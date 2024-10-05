
def is_multiply_prime(a):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    factors = []
    for i in range(2, a):
        if a % i == 0 and is_prime(i):
            factors.append(i)
            a //= i
            if len(factors) > 3:
                return False
    return len(factors) == 3 and is_prime(a)

print(is_multiply_prime(30))
print(is_multiply_prime(60))
print(is_multiply_prime(90))
print(is_multiply_prime(210))
print(is_multiply_prime(330))
print(is_multiply_prime(315))
<jupyter_output>
True
False
False
False
False
True
<jupyter_text>
**Question 2**
<jupyter_code>
