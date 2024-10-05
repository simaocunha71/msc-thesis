def do_algebra(operator, operand):
    import operator as op
    
    ops = {
        '+': op.add,
        '-': op.sub,
        '*': op.mul,
        '//': op.floordiv,
        '**': op.pow
    }
    
    result = operand[0]
    for op, val in zip(operator, operand[1:]):
        result = ops[op](result, val)
    
    return result

print(do_algebra(['+', '*', '-'], [2, 3, 4, 5]))  # should print 9
print(do_algebra(['+', '*', '-'], [1, 2, 3, 4, 5]))  # should print 6
print(do_algebra(['+', '*', '-'], [10, 20, 30, 40, 50]))  # should print 100