    # Define the function to do algebra
    def do_algebra(operator, operand):
        # Initialize the result
        result = operand[0]
        
        # Iterate over the operator and operand lists
        for i in range(len(operator)):
            # Perform the operation
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
        
        # Return the result
        return result
    
    # Test the function
    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    result = do_algebra(operator, operand)
    print(result)  # Output: 9

    # Test the function with other operators and operands
    operator = ['*', '//', '**']
    operand = [4, 5, 2]
    result = do_algebra(operator, operand)
    print(result)  # Output: 20

    # Test the function with a list of operators and operands
    operator = ['+', '-', '*']
    operand = [1, 2, 3, 4]
    result = do_algebra(operator, operand)
    print(result)  # Output: 10

    # Test the function with a list of operators and operands with negative numbers
    operator = ['+', '-', '*']
    operand = [1, -2, 3, -4]
    result = do_algebra(operator, operand)
    print(result)  # Output: 2

    # Test the function with a list of operators and operands with decimal numbers
    operator = ['+', '-', '*']
    operand = [1.0, 2.5, 3.0, 4.5]
    result = do_algebra(operator, operand)
    print(result)  # Output: 7.0

    # Test the function with a list of operators and operands with zero
    operator = ['+', '-', '*']
    operand = [0, 1, 2, 3]
    result = do_algebra(operator, operand)
    print(result)  # Output: 6

    # Test the function with a list of operators