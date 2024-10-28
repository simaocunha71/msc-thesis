def do_algebra(operator, operand):
    return eval(' '.join(str(x) for x in operand[:1])) + eval(' '.join(str(x) for x in operator + operand[1:])) if operator else operand[0]

print(do_algebra(['+', '*', '-'], [2, 3, 4, 5]))
print(do_algebra(['+', '*', '-'], [1, 2, 3, 4, 5]))