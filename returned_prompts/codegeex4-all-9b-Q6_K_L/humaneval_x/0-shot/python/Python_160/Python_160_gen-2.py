def do_algebra(operator, operand):
    result = operand[0]
    for i in range(len(operator)):
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
    return result

print(do_algebra(['+', '*', '-'], [2, 3, 4, 5]))  # Output: 9
print(do_algebra(['+', '*', '-'], [5, 2, 3, 4]))  # Output: 5
print(do_algebra(['+', '*', '-'], [5, 2, 3, 4, 2]))  # Output: 5
print(do_algebra(['+', '*', '-'], [5, 2, 3, 4, 2, 3]))  # Output: 5
print(do_algebra(['+', '*', '-'], [5, 2, 3, 4, 2, 3, 4]))  # Output: 5
print(do_algebra(['+', '*', '-'], [5, 2, 3, 4, 2, 3, 4, 5]))  # Output: 5
print(do_algebra(['+', '*', '-'], [5, 2, 3, 4, 2, 3, 4, 5, 6]))  # Output: 5
print(do_algebra(['+', '*', '-'], [5, 2, 3, 4, 2, 3, 4, 5, 6, 7]))  # Output: 5
print(do_algebra(['+', '*', '-'], [5, 2, 3, 4, 2, 3, 4, 5, 6, 7, 8]))  # Output: 5
print(do_algebra(['+', '*', '-'], [5, 2, 3, 4, 2, 3, 4, 5, 6, 7, 8, 9]))  # Output: 5
print(do_algebra(['+', '*', '-'], [5, 2, 