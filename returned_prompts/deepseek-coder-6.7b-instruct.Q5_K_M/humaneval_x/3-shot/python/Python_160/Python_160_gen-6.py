    import operator as op

    ops = {
        "+": op.add,
        "-": op.sub,
        "*": op.mul,
        "//": op.floordiv,
        "**": op.pow
    }

    result = operand[0]
    for i in range(1, len(operand)):
        result = ops[operator[i-1]](result, operand[i])

    return result


