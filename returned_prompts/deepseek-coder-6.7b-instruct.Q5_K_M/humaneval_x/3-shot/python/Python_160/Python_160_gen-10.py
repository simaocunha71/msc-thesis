    result = operand[0]
    for idx in range(len(operator)):
        if operator[idx] == '+':
            result += operand[idx + 1]
        elif operator[idx] == '-':
            result -= operand[idx + 1]
        elif operator[idx] == '*':
            result *= operand[idx + 1]
        elif operator[idx] == '//':
            result //= operand[idx + 1]
        elif operator[idx] == '**':
            result **= operand[idx + 1]

    return result

