    if numbers:
        return (sum(numbers), reduce(lambda x, y: x * y, numbers))
    else:
        return (0, 1)


