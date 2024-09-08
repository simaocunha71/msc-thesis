def count_Primes_nums(n):
    if n < 2:
        return 0
    primes = [True] * n
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n, p):
                primes[i] = False
        p += 1
    return sum(primes) - 2  # subtract 2 because we start from 0 and 1

assert count_Primes_nums(5) == 2

# Now, let's test it with some more test cases.

assert count_Primes_nums(10) == 4
assert count_Primes_nums(15) == 6
assert count_Primes_nums(20) == 8
assert count_Primes_nums(25) == 10
assert count_Primes_nums(30) == 12
assert count_Primes_nums(0) == 0
assert count_Primes_nums(1) == 0
<jupyter_output>
<empty_output>
<jupyter_text>
Question 4: Write a Python function that takes in a string and returns the number of vowels in the string.
<jupyter_code>
