    result = operand[0]
    for index in range(len(operator)):
        if operator[index] == '+':
            result += operand[index + 1]
        elif operator[index] == '-':
            result -= operand[index + 1]
        elif operator[index] == '*':
            result *= operand[index + 1]
        elif operator[index] == '//':
            result //= operand[index + 1]
        elif operator[index] == '**':
            result **= operand[index + 1]

    return result
