
    from functools import reduce
    
    return reduce(lambda x, y: x + y, map(lambda i: operator[i] * operand[i], range(len(operator))))

    # or
    
    return reduce(lambda x, y: x + y, map(lambda i: operator[i] * operand[i + 1], range(len(operator))))
