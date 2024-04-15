def optimize_ast(ast):
    return optimize_node(ast)

def optimize_node(node):
    if isinstance(node, dict):
        node_type = node.get('type')

        if node_type == 'binary_operation':
            left = optimize_node(node['left'])
            right = optimize_node(node['right'])
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
            operand = optimize_node(node['operand'])
            operator = node['operator']

            if operand['type'] == 'number':
                if operator == '-':
                    return {'type': 'number', 'value': -operand['value']}

            node['operand'] = operand
            return node

        else:
            for key, value in node.items():
                if isinstance(value, (dict, list)):
                    node[key] = optimize_node(value)
            return node

    elif isinstance(node, list):
        return [optimize_node(item) for item in node]

    else:
        return node