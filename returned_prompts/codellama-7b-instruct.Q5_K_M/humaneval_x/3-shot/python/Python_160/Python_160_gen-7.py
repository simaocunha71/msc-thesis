    result = operand[0]
    for index, operation in enumerate(operator):
        result = eval(str(result) + operation + str(operand[index + 1]))
    return result
