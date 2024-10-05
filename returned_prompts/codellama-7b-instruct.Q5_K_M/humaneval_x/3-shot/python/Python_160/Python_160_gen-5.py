    result = operand[0]
    for index, op in enumerate(operator):
        result = eval(str(result) + op + str(operand[index + 1]))

    return result


