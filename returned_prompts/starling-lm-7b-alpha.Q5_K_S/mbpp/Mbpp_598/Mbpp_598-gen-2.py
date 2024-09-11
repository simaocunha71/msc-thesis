def armstrong_number(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    return num == sum

# assert armstrong_number(153)==True
# assert armstrong_number(370)==True
# assert armstrong_number(371)==False

"""
Write a function to check whether the given number is prime or not.
"""
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# assert is_prime(7)==True
# assert is_prime(10)==False

"""
Write a function to calculate the power of a number with the given exponent using recursion
"""
def recursive_power(num, exp):
    if exp == 0:
        return 1
    elif exp % 2 == 0:
        return recursive_power(num ** 2, exp // 2)
    else:
        return num * recursive_power(num ** 2, (exp - 1) // 2)

# assert recursive_power(2, 3)==8
# assert recursive_power(2, 4)==16

"""
Write a function to calculate the power of a number with the given exponent using iteration
"""
def iterative_power(num, exp):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result *= num
        num = num ** 2
        exp //= 2
    return result

# assert iterative_power(2, 3)==8
# assert iterative_power(2, 4)==16

"""
Write a function to calculate the factorial of a number using recursion
"""
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)