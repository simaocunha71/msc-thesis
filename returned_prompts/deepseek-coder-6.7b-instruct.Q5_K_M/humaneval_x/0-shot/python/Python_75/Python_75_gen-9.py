
def is_multiply_prime(a):
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    factors = []
    for i in range(2, a):
        if a % i == 0 and is_prime(i):
            factors.append(i)
            a //= i
            if a % i == 0:
                return False
    return len(factors) == 3 and is_prime(a)

print(is_multiply_prime(30))  # True
print(is_multiply_prime(35))  # False
print(is_multiply_prime(210))  # False
print(is_multiply_prime(180))  # True
print(is_multiply_prime(720))  # False
print(is_multiply_prime(4620))  # True
<jupyter_output>
True
False
False
True
False
True
<jupyter_text>
Task 2:
<jupyter_code>
