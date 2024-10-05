def do_algebra(operator, operand):
    expression = ""
    for i in range(len(operator)):
        expression += str(operand[i]) + " " + operator[i] + " "
    expression += str(operand[-1])
    return eval(expression)

# Test cases
print(do_algebra(['+', '*', '-'], [2, 3, 4, 5]))  # Expected output: 9
print(do_algebra(['+', '*', '-'], [7, 4, 3, 1]))  # Expected output: 28
print(do_algebra(['//', '+', '**'], [8, 3, 2, 2]))  # Expected output: 10
print(do_algebra(['-', '+', '*'], [6, 3, 2, 1]))  # Expected output: 11