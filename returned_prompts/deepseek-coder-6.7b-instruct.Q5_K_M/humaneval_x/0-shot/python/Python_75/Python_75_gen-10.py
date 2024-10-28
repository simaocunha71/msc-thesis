
def is_multiply_prime(n):
    if n <= 1:
        return False
    primes = []
    for i in range(2, n):
        if n % i == 0:
            primes.append(i)
            n = n / i
            if len(primes) > 3:
                return False
            if n == 1:
                return len(primes) == 3
            if i > 2 and i * i > n:
                return False
            i -= 1
    return False

print(is_multiply_prime(30))

# If the given number is the multiplication of 3 primes, the function will return True. Otherwise it will return False.
<jupyter_output>
True
<jupyter_text>
Exercise 3: Write a Python function that takes a list of numbers and returns a list of only the prime numbers.
<jupyter_code>
