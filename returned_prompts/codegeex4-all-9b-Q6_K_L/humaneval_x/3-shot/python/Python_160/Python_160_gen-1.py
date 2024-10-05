    result = operand[0]

    for idx, op in enumerate(operator):
        if op == '+':
            result += operand[idx + 1]
        elif op == '-':
            result -= operand[idx + 1]
        elif op == '*':
            result *= operand[idx + 1]
        elif op == '//':
            result //= operand[idx + 1]
        elif op == '**':
            result **= operand[idx + 1]

    return result

