def is_not_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2): 
        return True
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return True
    return False

print(is_not_prime(2)) # False
print(is_not_prime(4)) # True
print(is_not_prime(15)) # True
print(is_not_prime(29)) # False
print(is_not_prime(33)) # True
print(is_not_prime(37)) # False

# Solution 2:
def is_not_prime(n):
    if n <= 1:
        return True
    elif n <= 3:
        return False
    elif n % 2 == 0 or n % 3 == 0:
        return True
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return True
        i += 6
    return False

print(is_not_prime(2)) # False
print(is_not_prime(4)) # True
print(is_not_prime(15)) # True
print(is_not_prime(29)) # False
print(is_not_prime(33)) # True
print(is_not_prime(37)) # False
<jupyter_output>
False
True
True
False
True
False
<jupyter_text>
Problem 2:Write a Python function to calculate the sum of the digits of a number. Use the function to calculate the sum of the digits of the number 12345.
<jupyter_code>
def sum_of_digits(n):
    sum = 0
    while n:
        sum += n % 10
        n //= 10
    return sum

print(sum_of_digits(12345)) # 15
<jupyter_output>
15
<jupyter_text>
