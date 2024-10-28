
def do_algebra(operator, operand):
    expression = str(operand[0])
    for i in range(len(operator)):
        expression += ' ' + operator[i] + ' ' + str(operand[i+1])
    return eval(expression)

# Test Cases
print(do_algebra(['+', '*', '-'], [2, 3, 4, 5])) # 9
print(do_algebra(['+', '*'], [2, 3, 4])) # 14
print(do_algebra(['-', '+'], [2, 3, 4])) # 5
print(do_algebra(['*', '+'], [2, 3, 4])) # 10
print(do_algebra(['/', '*'], [10, 2, 3])) # 6
<jupyter_output>
9
14
5
10
6
<jupyter_text>
Problem 4
<jupyter_code>
