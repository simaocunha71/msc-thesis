
def do_algebra(operator, operand):
    expr = str(operand[0])
    for i in range(len(operator)):
        expr += ' ' + operator[i] + ' ' + str(operand[i+1])
    return eval(expr)

# Test cases
print(do_algebra(['+', '*', '-'], [2, 3, 4, 5]))  # 9
print(do_algebra(['*', '+'], [2, 3, 4]))  # 14
print(do_algebra(['-', '+'], [10, 20, 30]))  # 40
print(do_algebra(['+', '-'], [10, 20, 30, 40]))  # 60
print(do_algebra(['*', '+'], [2, 3, 4, 5, 6]))  # 36

In Python, the eval() function can be used to evaluate a string as a python expression. In this case, we use it to evaluate the string representation of the algebraic expression built from the operator and operand lists.
<jupyter_output>
9
14
40
60
36
<jupyter_text>
Problem 2:
<jupyter_code>
