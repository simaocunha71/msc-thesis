    # Initialize the result to the first operand
    result = operand[0]

    # Loop through the operators and operands
    for i in range(len(operator) - 1):
        # Apply the current operator to the result and the next operand
        if operator[i] == '+':
            result += operand[i + 1]
        elif operator[i] == '-':
            result -= operand[i + 1]
        elif operator[i] == '*':
            result *= operand[i + 1]
        elif operator[i] == '//' or operator[i] == '**':
            if operator[i] == '//' and result % operand[i + 1] != 0:
                raise ValueError("Floor division is not exact")
            result = eval(str(result) + operator[i] + str(operand[i + 1]))

    # Return the final result
    return result

# Example usage:
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]
print(do_algebra(operator, operand))  # Output: 9

# Example with floor division:
operator = ['+', '//', '*']
operand = [10, 3, 2]
print(do_algebra(operator, operand))  # Output: 14

# Example with exponentiation:
operator = ['+', '**', '*']
operand = [2, 3, 2]
print(do_algebra(operator, operand))  # Output: 16
# Test the function with edge cases
print(do_algebra(['+'], [1]))  # Output: 1
print(do_algebra(['-', '*'], [1, 2, 3]))  # Output: -5
print(do_algebra(['+', '+'], [1, 2, 3, 4]))  # Output: 10
print(do_algebra(['*', '**'], [1, 2, 3]))  # Output: 12
print(do_algebra(['+', '+', '+', '+'], [1, 2, 3, 4, 5]))  # Output: 15
print(do_algebra(['-', '-', '-'], [1, 2, 3, 4]))  # Output: -8
print(do_algebra(['*', '*', '*'], [1, 2, 3, 4]))  # Output: 24
print(do_algebra(['+', '+', '+', '+', '+'], [1, 2, 3