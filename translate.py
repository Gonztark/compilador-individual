def translate_to_python(ast):
    python_code = ""
    for node in ast:
        python_code += translate_statement(node) + "\n"
    return python_code.strip()


def translate_expression(expr):
    if expr['type'] == 'binary_operation':
        left = translate_expression(expr['left'])
        right = translate_expression(expr['right'])
        return f"{left} {expr['operator']} {right}"
    elif expr['type'] == 'unary_operation':
        operand = translate_expression(expr['operand'])
        return f"{expr['operator']}{operand}"
    elif expr['type'] == 'number':
        if isinstance(expr['value'], int):
            return str(expr['value'])
        elif isinstance(expr['value'], float):
            return str(expr['value']).rstrip('0').rstrip('.')
    elif expr['type'] == 'variable':
        return expr['name']
    elif expr['type'] == 'comparison':
        left = translate_expression(expr['left'])
        right = translate_expression(expr['right'])
        return f"{left} {expr['operator']} {right}"
    elif expr['type'] == 'string':
        return f'"{expr["value"]}"'

def translate_function_declaration(node):
    name = node['name']
    params = ', '.join([param[1] for param in node['params']])
    body = translate_block(node['body'])

    global_vars = set()
    for statement in node['body']:
        global_vars.update(find_global_vars(statement))

    if global_vars:
        global_vars_declaration = "    global " + ", ".join(global_vars) + "\n"
        body = global_vars_declaration + body

    return f"def {name}({params}):\n{body}"

def find_global_vars(node):
    global_vars = set()
    if node['type'] == 'var_assignment':
        global_vars.add(node['name'])
    elif node['type'] == 'if':
        for statement in node['body']:
            global_vars.update(find_global_vars(statement))
    elif node['type'] == 'while':
        for statement in node['body']:
            global_vars.update(find_global_vars(statement))
    return global_vars

def translate_if_statement(node, indent_level=1):
    condition = translate_expression(node['condition'])
    body = translate_block(node['body'], indent_level + 1)
    return f"if {condition}:\n{body}"

def translate_if_else_statement(node, indent_level=1):
    condition = translate_expression(node['condition'])
    if_body = translate_block(node['if_body'], indent_level + 1)
    else_body = translate_block(node['else_body'], indent_level + 1)
    return f"if {condition}:\n{if_body}\nelse:\n{else_body}"

def translate_while_statement(node, indent_level=1):
    condition = translate_expression(node['condition'])
    body = translate_block(node['body'], indent_level + 1)
    return f"while {condition}:\n{body}"

def translate_block(block, indent_level=1):
    python_code = ""
    for statement in block:
        if statement['type'] in ['for', 'if', 'if_else', 'while']:
            python_code += " " * 4 * indent_level + translate_statement(statement, indent_level) + "\n"
        else:
            python_code += " " * 4 * indent_level + translate_statement(statement) + "\n"
    return python_code

def translate_statement(statement, indent_level=1):
    if statement['type'] == 'ignore':
        return ''
    if statement['type'] == 'var_declaration':
        if statement['value']['type'] == 'function_call':
            value = translate_function_call(statement['value'])
        else:
            value = translate_expression(statement['value'])
        return f"{statement['name']} = {value}"

    elif statement['type'] == 'var_assignment':
        # cuando es una llamada de función asignando a una variable
        if statement['value']['type'] == 'function_call':
            value = translate_function_call(statement['value'])
        else:
            value = translate_expression(statement['value'])
        return f"{statement['name']} = {value}"

    elif statement['type'] == 'function_declaration':
        return translate_function_declaration(statement)

    elif statement['type'] == 'if':
        return translate_if_statement(statement, indent_level)

    elif statement['type'] == 'if_else':
        return translate_if_else_statement(statement, indent_level)

    elif statement['type'] == 'while':
        return translate_while_statement(statement, indent_level)

    elif statement['type'] == 'for':
        variable = statement['init']['name']
        start = translate_expression(statement['init']['value'])
        end = translate_expression(statement['condition']['right'])
        step = None

        if statement['step']['type'] == 'var_assignment':
            if statement['step']['value']['type'] == 'binary_operation':
                step_left = translate_expression(statement['step']['value']['left'])
                step_right = translate_expression(statement['step']['value']['right'])
                if statement['step']['value']['operator'] == '+':
                    step = step_right
                elif statement['step']['value']['operator'] == '-':
                    step = f"-{step_right}"

        body = translate_block(statement['body'], indent_level + 1)

        if step:
            return f"for {variable} in range({start}, {end}, {step}):\n{body}"
        else:
            return f"for {variable} in range({start}, {end}):\n{body}"

    elif statement['type'] == 'print':
        #return f"print({translate_expression(statement['value'])})"
        return f"print({translate_print_arguments(statement['value'])})"

    elif statement['type'] == 'function_call':
        # funciones directas como statements
        return translate_function_call(statement)
    
    elif statement['type'] == 'read':
        return f"{statement['variable']} = input()"

    elif statement['type'] == 'return':
        return f"return {translate_expression(statement['value'])}"


def translate_function_call(node):
    name = node['name']
    arguments = ', '.join([translate_expression(arg) for arg in node['arguments']])
    return f"{name}({arguments})"

def translate_print_arguments(args):
    if args['type'] == 'concat':
        left = translate_print_arguments(args['left'])
        right = translate_print_arguments(args['right'])
        return f"{left} + {right}"
    elif args['type'] == 'string':
        return f'"{args["value"]}"'
    else:
        # Si es una variable y no es una cadena, aplicar str()
        if args['type'] == 'variable' and args['value']['type'] != 'string':
            return f"str({translate_expression(args)})"
        else:
            return translate_expression(args)
   
def translate_ast(ast, indent_level=0):
    result = ""
    indent = "  " * indent_level

    for node in ast:
        if node['type'] == 'var_declaration':
            result += f"{indent}var_declaration:\n"
            result += f"{indent}  name: {node['name']}\n"
            result += f"{indent}  value:\n"
            result += translate_ast([node['value']], indent_level + 2)
        elif node['type'] == 'function_declaration':
            result += f"{indent}function_declaration:\n"
            result += f"{indent}  name: {node['name']}\n"
            result += f"{indent}  params: {node['params']}\n"
            result += f"{indent}  body:\n"
            result += translate_ast(node['body'], indent_level + 2)
        elif node['type'] == 'var_assignment':
            result += f"{indent}var_assignment:\n"
            result += f"{indent}  name: {node['name']}\n"
            result += f"{indent}  value:\n"
            result += translate_ast([node['value']], indent_level + 2)
        elif node['type'] == 'binary_operation':
            print("QUEEEEE PASSSSAAAA" + str(node['left']))
            result += f"{indent}binary_operation:\n"
            result += f"{indent}  operator: {node['operator']}\n"
            result += f"{indent}  left:\n"
            result += translate_ast([node['left']], indent_level + 2)
            result += f"{indent}  right:\n"
            result += translate_ast([node['right']], indent_level + 2)
        elif node['type'] == 'variable':
            result += f"{indent}variable:\n"
            result += f"{indent}  name: {node['name']}\n"
            result += f"{indent}  value: {node['value']}\n"
        elif node['type'] == 'number':
            result += f"{indent}number: {node['value']}\n"
        elif node['type'] == 'print':
            result += f"{indent}print:\n"
            result += f"{indent}  value:\n"
            result += translate_ast([node['value']], indent_level + 2)
        elif node['type'] == 'if':
            result += f"{indent}if:\n"
            result += f"{indent}  condition:\n"
            result += translate_ast([node['condition']], indent_level + 2)
            result += f"{indent}  body:\n"
            result += translate_ast(node['body'], indent_level + 2)
        elif node['type'] == 'comparison':
            result += f"{indent}comparison:\n"
            result += f"{indent}  operator: {node['operator']}\n"
            result += f"{indent}  left:\n"
            result += translate_ast([node['left']], indent_level + 2)
            result += f"{indent}  right:\n"
            result += translate_ast([node['right']], indent_level + 2)
        elif node['type'] == 'while':
            result += f"{indent}while:\n"
            result += f"{indent}  condition:\n"
            result += translate_ast([node['condition']], indent_level + 2)
            result += f"{indent}  body:\n"
            result += translate_ast(node['body'], indent_level + 2)
        elif node['type'] == 'function_call':
            result += f"{indent}function_call:\n"
            result += f"{indent}  name: {node['name']}\n"
            result += f"{indent}  arguments: {node['arguments']}\n"
        elif node['type'] == 'string':
            result += f"{indent}string: {node['value']}\n"

    return result