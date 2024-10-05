def do_algebra(operator, operand):
    return eval(''.join(str(x) + operator[i] if i < len(operator) else str(x) for i, x in enumerate(operand)))

print(do_algebra(['+', '*', '-'], [2, 3, 4, 5]))  # 9
print(do_algebra(['-', '*', '+'], [2, 3, 4, 5]))  # -9
print(do_algebra(['+', '*', '-'], [2, 3, 4, 5, 6]))  # 2 + 3 * 4 - 5
print(do_algebra(['-', '*', '+'], [2, 3, 4, 5, 6]))  # 2 - 3 * 4 + 5
print(do_algebra(['+', '-', '*'], [2, 3, 4, 5, 6]))  # 2 + 3 - 4 * 5
print(do_algebra(['-', '+', '*'], [2, 3, 4, 5, 6]))  # 2 - 3 + 4 * 5