    result = operand[0]
    for i in range(len(operator)):
        op = operator[i]
        num = operand[i+1]
        if op == '+':
            result += num
        elif op == '-':
            result -= num
        elif op == '*':
            result *= num
        elif op == '//':
            result //= num
        elif op == '**':
            result **= num

    return result


