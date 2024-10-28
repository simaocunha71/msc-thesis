
def do_algebra(operator, operand):
    expression = str(operand[0])
    for i in range(1, len(operand)):
        expression += " " + operator[i-1] + " " + str(operand[i])
    return eval(expression)

# Test the function
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]
print(do_algebra(operator, operand))  # Output: 9

# Test the function with another set of inputs
operator = ['+', '//', '**']
operand = [2, 3, 4, 5]
print(do_algebra(operator, operand))  # Output: 11

# Test the function with another set of inputs
operator = ['*', '+']
operand = [1, 2, 3, 4]
print(do_algebra(operator, operand))  # Output: 21
<jupyter_output>
9
11
21
<jupyter_text>
Problem 4:
<jupyter_code>
