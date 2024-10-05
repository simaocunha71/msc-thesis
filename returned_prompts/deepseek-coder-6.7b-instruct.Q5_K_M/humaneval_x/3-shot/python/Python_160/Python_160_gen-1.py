    import operator
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '//': operator.floordiv,
        '**': operator.pow
    }

    result = operand[0]

    for idx, op in enumerate(operator):
        result = ops[op](result, operand[idx + 1])

    return result


