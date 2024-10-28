
    result = operand[0]
    for i in range(len(operator)):
        op = operator[i]
        val = operand[i + 1]
        if op == '+':
            result += val
        elif op == '-':
            result -= val
        elif op == '*':
            result *= val
        elif op == '//':
            result //= val
        else:
            result **= val
    return result
