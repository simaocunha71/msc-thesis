    result = operand[0]
    for i, op in enumerate(operator):
        result = eval(f'result {op} operand[{i + 1}]')
    return result


