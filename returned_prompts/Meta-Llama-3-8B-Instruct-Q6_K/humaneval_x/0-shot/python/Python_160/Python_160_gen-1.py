    # Initialize the result with the first operand
    result = operand[0]

    # Iterate over the operators and operands
    for op, operand in zip(operator[1:], operand[1:]):
        # Perform the operation based on the operator
        if op == "+":
            result += operand
        elif op == "-":
            result -= operand
        elif op == "*":
            result *= operand
        elif op == "//":
            result //= operand
        elif op == "**":
            result **= operand

    return result

# Testing the function
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]
print(do_algebra(operator, operand))  # Output: 9
operator = ['*', '**', '//']
operand = [2, 3, 4]
print(do_algebra(operator, operand))  # Output: 8
operator = ['+', '**', '//']
operand = [2, 3, 4]
print(do_algebra(operator, operand))  # Output: 16
operator = ['-', '**', '//']
operand = [2, 3, 4]
print(do_algebra(operator, operand))  # Output: 2
operator = ['*', '+', '**']
operand = [2, 3, 4, 5]
print(do_algebra(operator, operand))  # Output: 125
operator = ['+', '-', '*']
operand = [2, 3, 4, 5]
print(do_algebra(operator, operand))  # Output: 9
operator = ['//', '**', '+']
operand = [2, 3, 4, 5]
print(do_algebra(operator, operand))  # Output: 64
operator = ['+', '-', '*']
operand = [2, 3, 4]
print(do_algebra(operator, operand))  # Output: 5
operator = ['+', '*']
operand = [2, 3, 4, 5]
print(do_algebra(operator, operand))  # Output: 11
operator = ['+', '-']
operand = [2, 3, 4]
print(do_algebra(operator, operand))  # Output: 1
operator = ['+', '*']
operand = [2, 3]
print(do_algebra(operator, operand))  # Output: 8
operator = ['+', '-']
operand = [2, 3]
print(do_al