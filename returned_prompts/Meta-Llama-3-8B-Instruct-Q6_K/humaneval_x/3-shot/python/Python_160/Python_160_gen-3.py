    result = operand[0]
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
    return result
# test
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]
print(do_algebra(operator, operand))  # Output: 9
# test
operator = ['+', '*']
operand = [1, 2, 3, 4]
print(do_algebra(operator, operand))  # Output: 11
# test
operator = ['*', '**']
operand = [2, 3, 4]
print(do_algebra(operator, operand))  # Output: 144
# test
operator = ['+']
operand = [1, 2]
print(do_algebra(operator, operand))  # Output: 3
# test
operator = ['-', '**']
operand = [2, 3, 4]
print(do_algebra(operator, operand))  # Output: 64
# test
operator = ['//']
operand = [4, 2]
print(do_algebra(operator, operand))  # Output: 2
# test
operator = ['+', '-']
operand = [1, 2, 3]
print(do_algebra(operator, operand))  # Output: 0
# test
operator = ['+']
operand = [1]
print(do_algebra(operator, operand))  # Output: 1
# test
operator = ['*']
operand = [1, 2]
print(do_algebra(operator, operand))  # Output: 2
# test
operator = ['**']
operand = [2]
print(do_algebra(operator, operand))  # Output: 4
# test
operator = ['+']
operand = [1, 2, 3, 4, 5]
print(do_algebra(operator, operand))  # Output: 15
# test
operator = ['*']
operand = [1, 2, 3, 4, 5]
print(do_algebra(operator, operand))  # Output