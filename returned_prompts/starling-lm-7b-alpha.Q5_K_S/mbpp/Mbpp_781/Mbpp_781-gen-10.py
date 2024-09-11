"""
def count_divisors(n):
    # Initialize result
    res = 0

    # Note that this loop runs till square root
    i = 1
    while i <= math.sqrt(n):

        # If i is a divisor of n
        if (n % i == 0):

            # If divisors are equal, increment result by one
            if (n / i == i):
                res = res + 1

            else: # Else add two divisors
                res = res + 2

        i = i + 1
    return res

print(count_divisors(10))
"""

def count_divisors(n):
    i = 1
    while i * i <= n:
        if n % i:
            i += 1
        elif i * i != n:
            # If divisors are not equal, increment result by two
            n = n // i
            res += 2
        else:
            # If divisors are equal, increment result by one
            res += 1
            n //= i
    return res

print(count_divisors(10))

# To check whether count of divisors is even, you can check whether res is even or odd
def check_even(res):
    if res % 2 == 0:
        print(True)
    else:
        print(False)

# Test
check_even(count_divisors(10))

"""
Explanation:
The function count_divisors(n) counts the number of divisors of the given number n. It works by iterating over the numbers from 1 to the square root of n. If i is a divisor of n, it checks whether the divisors are equal. If they are equal, it increments the result by one. If they are not equal, it increments the result by two. This way, it counts all the divisors of the number.

To check whether the count of divisors is even, you can use the function check_even(res) which checks whether res is even or odd. If res is even, it prints True. If res is odd, it prints False.
"""