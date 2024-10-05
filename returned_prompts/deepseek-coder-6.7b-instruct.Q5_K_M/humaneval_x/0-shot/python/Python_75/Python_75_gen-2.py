
def is_multiply_prime(a):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    factors = 0
    for i in range(2, a):
        if a % i == 0 and is_prime(i):
            factors += 1
    return factors == 3

print(is_multiply_prime(30))  # True

This function works by first defining a helper function `is_prime` that checks if a number is prime by checking if it has any factors other than 1 and itself. It then iterates through all numbers from 2 up to `a` and checks if `a` is divisible by the current number and if the current number is prime. If it is, it increments a counter `factors`. Finally, it returns whether the number of factors equals 3.
<jupyter_output>
<empty_output>
<jupyter_text>
4. Given a string, compute recursively a new string where all the 'x' chars have been removed.
<jupyter_code>
