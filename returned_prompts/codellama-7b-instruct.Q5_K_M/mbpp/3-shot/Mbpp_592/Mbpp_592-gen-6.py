
from itertools import accumulate, takewhile
from math import factorial
def sum_Of_product(n):
    def consecutive_binomial_coefficients(n):
        return list(takewhile(lambda x: x[1] <= n, enumerate(accumulate(factorial))))
    return sum(x*y for x, y in consecutive_binomial_coefficients(n))


