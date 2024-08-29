def is_not_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2): 
        return True
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return True
    return False

print(is_not_prime(2))  # False
print(is_not_prime(4))  # True
print(is_not_prime(9))  # True
print(is_not_prime(11))  # False
print(is_not_prime(15))  # True
print(is_not_prime(17))  # False
print(is_not_prime(21))  # True
print(is_not_prime(23))  # False
print(is_not_prime(25))  # True
print(is_not_prime(27))  # True
print(is_not_prime(29))  # False
print(is_not_prime(31))  # False
<jupyter_output>
False
True
True
False
True
False
True
False
True
True
False
False
False
<jupyter_text>
Question 3
<jupyter_code>
