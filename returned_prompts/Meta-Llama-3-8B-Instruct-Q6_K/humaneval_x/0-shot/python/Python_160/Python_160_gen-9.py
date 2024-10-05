    # Initialize the result with the first element of the operand list
    result = operand[0]

    # Loop through the operator and operand lists
    for i in range(len(operator)):
        # Get the current operator and operand
        op = operator[i]
        num = operand[i + 1]

        # Perform the operation based on the operator
        if op == '+':
            result += num
        elif op == '-':
            result -= num
        elif op == '*':
            result *= num
        elif op == '//':
            result //= num
        elif op == '**':
            result **= num

    # Return the final result
    return result
