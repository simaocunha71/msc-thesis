def sum_product(numbers):
    if numbers:
        return (sum(numbers), prod(numbers))
    else:
        return (0, 1)

def prod(numbers):
    p = 1
    for n in numbers:
        p *= n
    return p

