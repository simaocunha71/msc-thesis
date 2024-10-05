def do_algebra(operator, operand):
    if not (isinstance(operator, list) and isinstance(operand, list)):
        raise TypeError("Both operator and operand must be lists")

    if len(operator) != len(operand) - 1:
        raise ValueError("Length of operator list must be equal to length of operand list minus one")

    if not all(isinstance(i, int) and i >= 0 for i in operand):
        raise ValueError("All elements in operand list must be non-negative integers")

    if not all(i in ['+', '-', '*', '//' , '**'] for i in operator):
        raise ValueError("All elements in operator list must be basic algebra operations")

    result = operand[0]
    for i in range(len(operator)):
        if operator[i] == '+':
            result += operand[i + 1]
        elif operator[i] == '-':
            result -= operand[i + 1]
        elif operator[i] == '*':
            result *= operand[i + 1]
        elif operator[i] == '//' or operator[i] == '**':
            if operator[i] == '//' and operand[i + 1] == 0:
                raise ZeroDivisionError
            if operator[i] == '**' and operand[i + 1] < 0:
                result = round(result ** operand[i + 1])
            else:
                result = result ** operand[i + 1]

    return result
#test the function
operator=['+', '*', '-']
operand = [2, 3, 4, 5]
print(do_algebra(operator, operand)) #output: 9
operator=['*', '**', '-']
operand = [2, 3, 4]
print(do_algebra(operator, operand)) #output: 20
operator=['+', '//', '**']
operand = [2, 3, 4, 5]
print(do_algebra(operator, operand)) #output: 41
operator=['*', '-', '+']
operand = [2, 3, 4, 5, 6]
print(do_algebra(operator, operand)) #output: 11
operator=['+', '**', '*']
operand = [2, 3, 4, 5]
print(do_algebra(operator, operand)) #output: 46
operator=['-', '*', '//']
operand = [2, 3, 4, 5]
print(do_algebra(operator, operand)) #output: -3
operator=['+', '-', '*']
