# Here's a solution to the problem.

def do_algebra(operator, operand):
    # Initialize a stack
    stack = []
    # Initialize an operator string
    op_str = ""
    # Iterate over the operator list
    for i in range(len(operator) - 1):
        # If the current operator is multiplication, division, or exponentiation,
        # add the current operator to the operator string, and the current operand to the stack
        if operator[i] == '*':
            op_str += "*"
        elif operator[i] == '/':
            op_str += "/"
        elif operator[i] == '**':
            op_str += "**"
        else:
            # Otherwise, append the operator to the stack
            stack.append(operator[i])
            # Append the current operand to the operator string
            op_str += str(operand[i])
    # Append the last operator to the stack
    stack.append(operator[-1])
    # Append the last operand to the operator string
    op_str += str(operand[-1])
    # Initialize a result variable
    result = 0
    # Iterate over the stack
    for i in range(len(stack)):
        # If the current element is an operator, evaluate the expression using the result variable and append the result to the operator string
        if type(stack[i]) == str:
            if stack[i] == '+':
                result += operand[i]
            elif stack[i] == '-':
                result -= operand[i]
            elif stack[i] == '*':
                result *= operand[i]
            elif stack[i] == '/':
                result /= operand[i]
            elif stack[i] == '**':
                result = result ** operand[i]
        # If the current element is an integer, append the integer to the result variable
        else:
            result += stack[i]
    # Return the result
    return result

# Test cases
print(do_algebra(['+', '*', '-'], [2, 3, 4, 5]))  # 9
print(do_algebra(['