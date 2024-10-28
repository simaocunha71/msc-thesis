
def is_multiply_prime(a):
    prime_factors = []
    for i in range(2, int(a ** 0.5) + 1):
        while a % i == 0:
            prime_factors.append(i)
            a /= i
            if a % i != 0:
                break
    if a > 1:
        prime_factors.append(a)

    if len(prime_factors) == 3 and prime_factors.count(prime_factors[0]) == 1 and prime_factors.count(prime_factors[1]) == 1 and prime_factors.count(prime_factors[2]) == 1:
        return True
    else:
        return False
<jupyter_output>
<empty_output>
<jupyter_text>
Test cases:
<jupyter_code>
print(is_multiply_prime(30))  # Expected: True
print(is_multiply_prime(31))  # Expected: False
print(is_multiply_prime(32))  # Expected: False
print(is_multiply_prime(60))  # Expected: True
print(is_multiply_prime(97))  # Expected: False
<jupyter_output>
True
False
False
True
False
<jupyter_text>
Explanation:The function is_multiply_prime works by first finding all prime factors of the input number 'a'. It does this by iterating over all integers from 2 up to the square root of 'a' (since a factor of 'a' cannot be larger than sqrt(a)). If 'a' is divisible by the current integer, it is a prime factor, and the function appends it to the prime_factors list and divides 'a' by the factor. The process is repeated until 'a' is no longer divisible by the current integer. If 'a' is greater than 1 at the end of the function, it means 'a' is a prime factor and is appended to the prime_factors list. Finally, the function checks if there are exactly 