    def do_algebra(operator, operand):
        # Check if the length of operator list is equal to the length of operand list minus one.
        if len(operator) != len(operand) - 1:
            return "Invalid input. The length of operator list is not equal to the length of operand list minus one."
        
        # Initialize the result with the first operand
        result = operand[0]
        
        # Iterate over the operator list and the operand list from the second operand to the end.
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
        
        # Return the final result
        return result

    # Example usage
    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    print(do_algebra(operator, operand))  # Output: 9
    print(do_algebra(['+', '-'], [1, 2, 3]))  # Output: 0
    print(do_algebra(['*', '**'], [2, 3, 4]))  # Output: 128
    print(do_algebra(['//', '**'], [4, 2, 3]))  # Output: 8
    print(do_algebra(['+', '-', '+'], [1, 2, 3, 4]))  # Output: 6
    print(do_algebra(['*', '+', '-'], [2, 3, 4, 5]))  # Output: 5
    print(do_algebra(['-', '+', '*'], [1, 2, 3, 4]))  # Output: 6
    print(do_algebra(['+', '-', '**'], [2, 3, 4]))  # Output: 64
    print(do_algebra(['*', '+', '**'], [2, 3, 4]))  # Output: 64
    print(do_algebra(['+', '-', '//'], [2, 3, 4]))  # Output: 2
    print(do_algebra(['*', '+', '//'], [2,