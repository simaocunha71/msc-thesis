def do_algebra(operator, operand):
    result = operand[0]
    for i in range(1, len(operand)):
        if operator[i-1] == '+':
            result += operand[i]
        elif operator[i-1] == '-':
            result -= operand[i]
        elif operator[i-1] == '*':
            result *= operand[i]
        elif operator[i-1] == '//':
            result //= operand[i]
        elif operator[i-1] == '**':
            result **= operand[i]
    return result

# Test cases
print(do_algebra(['+', '*', '-'], [2, 3, 4, 5]))  # Expected output: 9
print(do_algebra(['+', '*', '-', '//'], [2, 3, 4, 5, 6]))  # Expected output: 8
print(do_algebra(['**', '*', '-', '+'], [2, 3, 4, 5, 6]))  # Expected output: 50
print(do_algebra(['**', '*', '-', '+'], [2, 3, 4, 5, 6, 7]))  # Expected output: 50
print(do_algebra(['**', '*', '-', '+'], [2, 3, 4, 5, 6, 7, 8]))  # Expected output: 50