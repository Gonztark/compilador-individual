var_declarations = []
var_assignment = []
variable = []

def optimize_ast(ast, symbol_table):
    global var_declarations
    global var_assignment
    global variable
    var_declarations = []
    var_assignment = []
    variable = []
    get_items(ast)
    newast = optimize_node(ast, symbol_table)
    return optimize_node(newast, symbol_table)

def get_items(node):
    if isinstance(node, dict):
        node_type = node.get('type')
        if node_type == 'var_declaration':
            var_declarations.append(node['name'])

        elif node_type == 'var_assignment':
            var_assignment.append(node['name'])

        elif node_type == 'read':
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            var_assignment.append(node['variable'])
        
        elif node_type == 'variable':
            if node['name'] not in variable:
                variable.append(node['name'])
                print(variable)

        else:
            for key, value in node.items():
                if isinstance(value, (dict, list)):
                    get_items(value)
            return node
        

    elif isinstance(node, list):
        return [get_items(item) for item in node]
    


def optimize_node(node, symbol_table):
    print(var_assignment)
    if isinstance(node, dict):
        node_type = node.get('type')

        if node_type == 'function_declaration':
            # No optimizar el cuerpo de la función
            return node

        if node_type == 'binary_operation':
            left = optimize_node(node['left'], symbol_table)
            right = optimize_node(node['right'], symbol_table)
            operator = node['operator']

            if left['type'] == 'number' and right['type'] == 'number':
                if operator == '+':
                    return {'type': 'number', 'value': left['value'] + right['value']}
                elif operator == '-':
                    return {'type': 'number', 'value': left['value'] - right['value']}
                elif operator == '*':
                    return {'type': 'number', 'value': left['value'] * right['value']}
                elif operator == '/':
                    if right['value'] != 0:
                        return {'type': 'number', 'value': left['value'] / right['value']}
                    else:
                        raise ValueError("División por cero")

            node['left'] = left
            node['right'] = right
            return node


        elif node_type == 'unary_operation':
            operand = optimize_node(node['operand'], symbol_table)
            operator = node['operator']

            if operand['type'] == 'number':
                if operator == '-':
                    return {'type': 'number', 'value': -operand['value']}

            node['operand'] = operand
            return node
        
        elif node_type == 'var_declaration':
            if node['name'] not in var_assignment:
                return {'type': 'ignore'}
            return node
        
        elif node_type == 'variable':
            if node['name'] not in var_assignment:
                print("VARRRRIABLEEE:"+node['name'])
                if node['name'] in symbol_table:
                    var_info = symbol_table[node['name']]
                    var_value = var_info['value']
                    print(var_value)
                    return var_value
                    #return f"{var_type}: {var_value}"
                else:
                    print("Variable no encontrada en la tabla de símbolos")
            return node

        else:
            for key, value in node.items():
                if isinstance(value, (dict, list)):
                    node[key] = optimize_node(value,symbol_table)
            return node
    


    elif isinstance(node, list):
        return [optimize_node(item, symbol_table) for item in node]

    else:
        return node