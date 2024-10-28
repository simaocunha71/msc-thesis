def do_algebra(operator, operand):
    return eval(''.join(['{}{}'.format(op, num) for op, num in zip(operator, operand)]))

operator = ['+', '*', '-']
array = [2, 3, 4, 5]
print(do_algebra(operator, array)) # => 9