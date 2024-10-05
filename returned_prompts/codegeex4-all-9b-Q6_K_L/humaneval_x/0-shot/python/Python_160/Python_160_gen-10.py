def do_algebra(operator, operand):
    exp = str(operand[0])
    for i in range(1, len(operand)):
        exp += " " + operator[i-1] + " " + str(operand[i])
    return eval(exp)

print(do_algebra(['+', '*', '-'], [2, 3, 4, 5]))