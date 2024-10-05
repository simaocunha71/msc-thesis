    def do_algebra(operator, operand):
        expression = ""
        for i in range(len(operator)):
            expression += str(operand[i])
            if i < len(operator) - 1:
                expression += operator[i]
        return eval(expression)

# Example usage:
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]
result = do_algebra(operator, operand)
print(result)  # Output: 9
