
def do_algebra(operator, operand):
    result = operand[0]
    for i in range(1, len(operand)):
        result = operator[i - 1](result, operand[i])
    return result


