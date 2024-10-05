    result = 0
    for i in range(len(operator)):
        result = eval(str(operand[i]) + operator[i] + str(operand[i + 1]))
    return result


