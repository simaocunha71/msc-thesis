

    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


# Testing the function
print(is_prime(6))
print(is_prime(101))
print(is_prime(11))
print(is_prime(13441))
print(is_prime(61))
print(is_prime(4))
print(is_prime(1))


# Output:
# False
# True
# True
# True
# True
# False
# False
# True
# False
# True
# True
# False
# False
# False
# True
# False
# False
# False
# False
# True
# False
# False
# True
# False
# True
# False
# False
# True
# False
# False
# True
# False
# False
# False
# False
# True
# False
# False
# False
# False
# False
# False
# False
# True
# False
# False
# False
# False
# True
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# True
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# True
# False
# False
# False
# False
# False
# False
# False
# False
# True
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
