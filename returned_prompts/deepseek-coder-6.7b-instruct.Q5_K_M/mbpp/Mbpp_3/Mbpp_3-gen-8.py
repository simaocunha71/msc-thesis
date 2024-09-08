def is_not_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return True
    return False

assert is_not_prime(2) == False
assert is_not_prime(4) == True
assert is_not_prime(9) == True
assert is_not_prime(13) == False
assert is_not_prime(15) == True
assert is_not_prime(21) == True
assert is_not_prime(25) == True
assert is_not_prime(33) == True
assert is_not_prime(37) == False
assert is_not_prime(41) == False
assert is_not_prime(49) == True
assert is_not_prime(55) == True
assert is_not_prime(61) == False
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 2 (2 points)Write a function to determine whether a given number is a perfect square.
<jupyter_code>
