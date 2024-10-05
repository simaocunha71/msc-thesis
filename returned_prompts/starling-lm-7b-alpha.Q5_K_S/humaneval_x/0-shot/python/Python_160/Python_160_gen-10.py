# Here are some notes about Python's operators precedence:
# 1. Exponentiation ( ** )
# 2. Multiplication ( * ) and Floor division ( // )
# 3. Addition ( + ) and Subtraction ( - )

# Python's expression evaluation is from left to right, so the precedence of operator is
# important to correctly evaluate the expression.

def do_algebra(operator, operand):
    result = operand[0]
    for i in range(0, len(operator)):
        if operator[i] == '+':
            result += operand[i + 1]
        elif operator[i] == '-':
            result -= operand[i + 1]
        elif operator[i] == '*':
            result *= operand[i + 1]
        elif operator[i] == '//':
            result //= operand[i + 1]
        elif operator[i] == '**':
            result = result ** operand[i + 1]
    return result

# Testing the function:
print(do_algebra(['+', '*', '-'], [2, 3, 4, 5]))  # It should return 9

# It should return 15:
print(do_algebra(['-', '*', '+'], [2, 3, 4, 5]))

# It should return 3:
print(do_algebra(['//', '+'], [10, 2]))

# It should return 32:
print(do_algebra(['*', '*', '*'], [2, 3, 4]))

# It should return 2:
print(do_algebra(['+', '-'], [10, 2]))

# It should return 20:
print(do_algebra(['**', '+'], [2, 3]))

# It should return 10:
print(do_algebra(['//', '*'], [10, 2]))

# It should return 15:
print(do_algebra(['*', '-'], [2, 3, 4]))

# It should return 20:
print(do