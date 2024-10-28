
def do_algebra(operator, operand):
    result = operand[0]
    for i, j in zip(operator, operand[1:]):
        if i == '+':
            result += j
        if i == '-':
            result -= j
        if i == '*':
            result *= j
        if i == '//':
            result //= j
        if i == '**':
            result **= j
    return result
