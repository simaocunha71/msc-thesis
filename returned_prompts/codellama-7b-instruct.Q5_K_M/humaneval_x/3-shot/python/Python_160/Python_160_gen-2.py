    result = 0
    for i in range(len(operand)):
        if i == 0:
            result = operand[i]
        else:
            result = operator[i - 1](result, operand[i])

    return result
