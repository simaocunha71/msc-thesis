    result = operand[0]
    for idx, op in enumerate(operator):
        if idx == 0:
            continue
        result = eval(f"result {op} operand[{idx}]")
    return result


