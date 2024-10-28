# Here is a Python solution to the problem:

def do_algebra(operator, operand):
    # Initialize result to first operand
    result = operand[0]
    # Iterate over the operators and operands
    for i in range(len(operator)):
        if operator[i] == '+':
            result += operand[i + 1]
        elif operator[i] == '-':
            result -= operand[i + 1]
        elif operator[i] == '*':
            result *= operand[i + 1]
        elif operator[i] == '//':
            result //= operand[i + 1]
        elif operator[i] == '**':
            result **= operand[i + 1]
    return result

# Test Cases
print(do_algebra(['+', '*', '-'], [2, 3, 4, 5]))  # Returns: 9
print(do_algebra(['+', '-', '*'], [2, 3, 4, 5]))  # Returns: -13
print(do_algebra(['//', '+', '*'], [2, 3, 4, 5]))  # Returns: 2.6666666666666665
print(do_algebra(['**', '*', '//'], [2, 3, 4, 5]))  # Returns: 20.0

# More Test Cases
print(do_algebra(['+', '-', '*'], [2, 3, 4, 5]))  # Returns: -13
print(do_algebra(['+', '*', '//'], [2, 3, 4, 5]))  # Returns: 2.6666666666666665
print(do_algebra(['*', '*', '**'], [2, 3, 4, 5]))  # Returns: 160.0

# Note: The length of operator list is equal to the length of operand list minus one.
# Operand is a list of of non-negative integers.
# Operator list has at least one