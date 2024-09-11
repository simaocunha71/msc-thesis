"""
The function is_all_positive checks whether all the numbers in a tuple are positive. The function max_product_tuple then finds the maximum product between numbers in pairs of tuples within a given list of tuples. Here is a step-by-step explanation of how it works:

The function is_all_positive checks if all the numbers in a tuple are positive. This function is used in the max_product_tuple function to find out whether we need to multiply all the numbers in the tuple or just the two maximum numbers.

The function max_product_tuple first checks whether all the tuples have all positive numbers. If they do, it multiplies all the numbers in each tuple and returns the maximum product. If not, it multiplies all the positive numbers and the product of the two maximum numbers. It returns the maximum of these two products.
"""

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
                max(reduce(lambda x, y: x * y, [max(x) for x in t if is_all_positive(x)]) * reduce(lambda x, y: x * y, [max(y) for y in t if is_all_pos