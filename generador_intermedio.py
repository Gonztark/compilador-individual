def translate_ast(ast):
    intermediate_code = []
    temp_var_count = 0
    label_count = 0

    def generate_temp_var():
        nonlocal temp_var_count
        temp_var = f"t{temp_var_count}"
        temp_var_count += 1
        return temp_var

    def generate_label():
        nonlocal label_count
        label = f"L{label_count}"
        label_count += 1
        return label

    def translate_node(node):
        if node['type'] == 'var_declaration':
            value = translate_node(node['value'])
            intermediate_code.append(f"{node['name']} = {value}")
        elif node['type'] == 'var_assignment':
            value = translate_node(node['value'])
            intermediate_code.append(f"{node['name']} = {value}")
        elif node['type'] == 'binary_operation':
            left = translate_node(node['left'])
            right = translate_node(node['right'])
            temp_var = generate_temp_var()
            intermediate_code.append(f"{temp_var} = {left} {node['operator']} {right}")
            return temp_var
        elif node['type'] == 'variable':
            return node['name']
        elif node['type'] == 'number':
            return str(node['value'])
        elif node['type'] == 'print':
            value = translate_node(node['value'])
            intermediate_code.append(f"print {value}")
        elif node['type'] == 'if':
            condition = translate_node(node['condition'])
            if_true_label = generate_label()
            if_false_label = generate_label()
            intermediate_code.append(f"if {condition} goto {if_true_label}")
            intermediate_code.append(f"goto {if_false_label}")
            intermediate_code.append(f"{if_true_label}:")
            for statement in node['body']:
                translate_node(statement)
            intermediate_code.append(f"{if_false_label}:")
        elif node['type'] == 'comparison':
            left = translate_node(node['left'])
            right = translate_node(node['right'])
            temp_var = generate_temp_var()
            intermediate_code.append(f"{temp_var} = {left} {node['operator']} {right}")
            return temp_var
        elif node['type'] == 'while':
            condition = translate_node(node['condition'])
            while_start_label = generate_label()
            while_end_label = generate_label()
            intermediate_code.append(f"{while_start_label}:")
            intermediate_code.append(f"if {condition} goto {while_end_label}")
            intermediate_code.append(f"goto {while_start_label}")
            intermediate_code.append(f"{while_end_label}:")
            for statement in node['body']:
                translate_node(statement)
            intermediate_code.append(f"goto {while_start_label}")
        elif node['type'] == 'function_call':
            args = ', '.join([translate_node(arg) for arg in node['arguments']])
            intermediate_code.append(f"call {node['name']}({args})")
        elif node['type'] == 'string':
            return f'"{node["value"]}"'
        elif node['type'] == 'function_declaration':
            intermediate_code.append(f"func {node['name']}:")
            for statement in node['body']:
                translate_node(statement)
            intermediate_code.append(f"return")

    for node in ast:
        translate_node(node)

    return '\n'.join(intermediate_code)