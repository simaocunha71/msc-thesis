from functools import reduce
def is_all_positive(t):
    return all(x > 0 for x in t)
def max_product_tuple(t):
    # If all tuples have all positive numbers, product of all numbers
    if all(is_all_positive(x) for x in t):
        return reduce(lambda x, y: x * y,
                      reduce(lambda x, y: [max(x[0], y[0]), max(x[1], y[1])] if is_all_positive(x) and is_all_positive(y)
                                         else [reduce(lambda x, y: x * y, x), reduce(lambda x, y: x * y, y)]
                            , t))
    # Else product of all positive numbers and product of two max numbers
    else:
        return max(reduce(lambda x, y: x * y, x) * reduce(lambda x, y: x * y, [max(x) for x in t if is_all_positive(x)])
                  for x in t),