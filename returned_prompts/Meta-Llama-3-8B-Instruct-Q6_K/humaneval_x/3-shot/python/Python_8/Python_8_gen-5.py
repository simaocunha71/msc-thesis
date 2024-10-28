    if not numbers:
        return 0, 1

    return sum(numbers), eval('*'.join(map(str, numbers)))  # Using eval for product calculation
    # return sum(numbers), functools.reduce(operator.mul, numbers, 1)  # Using functools.reduce and operator.mul for product calculation


