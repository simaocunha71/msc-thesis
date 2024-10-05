    result = operand[0]
    for idx, operator in enumerate(operator):
        if operator == '+':
            result += operand[idx + 1]
        elif operator == '-':
            result -= operand[idx + 1]
        elif operator == '*':
            result *= operand[idx + 1]
        elif operator == '//':
            result //= operand[idx + 1]
        elif operator == '**':
            result **= operand[idx + 1]

    return result

