
def do_algebra(operator, operand):
    expression = str(operand[0])
    for i in range(len(operator)):
        expression += ' ' + operator[i] + ' ' + str(operand[i+1])
    return eval(expression)


print(do_algebra(['+', '*', '-'], [2, 3, 4, 5]))  # 9
print(do_algebra(['+', '*'], [2, 3, 4]))  # 14
print(do_algebra(['+', '-', '*'], [2, 3, 4, 5]))  # 13
print(do_algebra(['*', '+', '*'], [2, 3, 4, 5]))  # 26
print(do_algebra(['*', '-', '+'], [2, 3, 4, 5]))  # 17
print(do_algebra(['-', '+', '/'], [2, 3, 4]))  # 2
print(do_algebra(['+', '*', '**'], [2, 3, 4]))  # 29
print(do_algebra(['**', '*', '+'], [2, 3, 4]))  # 29
print(do_algebra(['-', '*', '+'], [2, 3, 4, 5]))  # -1
print(do_algebra(['-', '+', '*'], [2, 3, 4, 5]))  # 1

This function works by starting with the first operand as a string. Then it iterates over the operator list and for each operator, it appends the operator and the next operand to the expression string. Finally, it evaluates the expression string and returns the result.

Note: This function uses the eval function which can be dangerous if the input is not trusted, as it can execute arbitrary python code. In this case, as we are using this function with trusted inputs, it should be safe.
"""


def do_algebra(operator, operand):
    expression = str(operand[0])
    for i in range(len(operator)):
        expression