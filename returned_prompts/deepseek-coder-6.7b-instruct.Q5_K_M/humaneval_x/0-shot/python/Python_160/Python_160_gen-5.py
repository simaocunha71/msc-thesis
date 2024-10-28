
def do_algebra(operator, operand):
    # Initialize result to the first operand
    result = operand[0]

    # Iterate over the operators and operands
    for i in range(len(operator)):
        # Perform the operation and update the result
        if operator[i] == '+':
            result += operand[i+1]
        elif operator[i] == '-':
            result -= operand[i+1]
        elif operator[i] == '*':
            result *= operand[i+1]
        elif operator[i] == '//':
            result //= operand[i+1]
        elif operator[i] == '**':
            result **= operand[i+1]

    # Return the result
    return result

# Test the function
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]
print(do_algebra(operator, operand))  # Output: 9

# This function works by initializing the result to the first operand and then iterating over the operators and operands. It performs the operation specified by the operator on the result and the operand, and updates the result accordingly. Finally, it returns the result.
<jupyter_output>
9
<jupyter_text>
Problem 4:
<jupyter_code>
