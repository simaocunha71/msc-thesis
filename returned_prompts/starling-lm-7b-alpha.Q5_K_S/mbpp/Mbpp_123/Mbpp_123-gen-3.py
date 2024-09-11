def amicable_numbers_sum(n):
    """
    >>> amicable_numbers_sum(999)
    504
    """
    from sympy import summation, sigma, symbols, Eq, solve, sqrt
    # The sum of proper amicable numbers from 1 to n is the sum of the proper divisors of
    # each number less than or equal to n, squared, divided by two.
    # A number x is a proper divisor of y if and only if x is a divisor of y and x < y
    # The sum of the proper divisors of y is sigma(y) - y
    # sigma(y) is the sum of the divisors of y.
    # The number of proper divisors of y is (sigma(y) - y) / y
    # The sum of the squares of the proper divisors of y is the sum of the squares of the divisors of y, divided by 2
    # The sum of the squares of the divisors of y is sigma(y^2) / 2
    # The sum of the squares of the proper divisors of y is (sigma(y^2) - y^2) / 2
    # The sum of the proper divisors of y squared is (sigma(y^2) - y^2) / 2
    # The sum of the proper divisors of y, squared, is (sigma(y) - y) / 2
    # The sum of the proper divisors of y, squared, is (sigma(y) - y) / 2
    # The sum of the proper divisors of y, squared, is (sigma(y) - y) / 2
    # The sum of the proper divisors of y, squared, is (sigma(y) - y) / 2
    # The sum of the proper divisors of y, squared, is (sigma(y) - y) / 2
    # The sum of the proper divisors of y, squared, is (sigma(y) - y) / 2
    # The sum of the proper divisors of y, squared, is (sigma(y) - y) / 2
   