def cummulative_sum(tuples):
    total = 0
    for tup in tuples:
        total += sum(tup)
    return total

print(cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]))  # 30

"""
Write a function to find the cumulative product of all the values that are present in the given tuple list.
assert cummulative_product([(1, 3), (5, 6, 7), (2, 6)]) == 7200
"""

def cummulative_product(tuples):
    total = 1
    for tup in tuples:
        total *= prod(tup)
    return total

print(cummulative_product([(1, 3), (5, 6, 7), (2, 6)]))  # 7200

"""
Write a function to find the cumulative sum and product of all the values that are present in the given tuple list. The function should return a tuple containing the sum and product.
assert cummulative_sum_and_product([(1, 3), (5, 6, 7), (2, 6)]) == (30, 7200)
"""

def cummulative_sum_and_product(tuples):
    sum_total = 0
    prod_total = 1
    for tup in tuples:
        sum_total += sum(tup)
        prod_total *= prod(tup)
    return (sum_total, prod_total)

print(cummulative_sum_and_product([(1, 3), (5, 6, 7), (2, 6)]))  # (30, 7200)

"""
Write a function to find the cumulative sum and product of all the values that are present in the given tuple list, but only if the tuple has at least two elements.
assert cummulative_sum_and_product_with_two_elements([(1, 3), (5, 6, 7), (2)]) == (30,