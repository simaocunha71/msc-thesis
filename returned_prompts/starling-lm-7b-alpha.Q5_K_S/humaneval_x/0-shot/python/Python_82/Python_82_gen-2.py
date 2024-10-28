
def prime_length(string):
    # Check if the length of the string is a prime number
    if len(string) % 2 == 0:
        return False
    else:
        for i in range(3, int(len(string) ** 0.5) + 1, 2):
            if len(string) % i == 0:
                return False
        return True

# Test the function
print(prime_length('Hello'))  # True
print(prime_length('abcdcba'))  # True
print(prime_length('kittens'))  # True
print(prime_length('orange'))  # False

# More test cases
print(prime_length('world'))  # False
print(prime_length('test'))  # False
print(prime_length('programming'))  # True


# To check if a number is prime, we can use the following function:

def is_prime(num):
    if num % 2 == 0 and num > 2:  # If the number is even and not 2
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

# Test the function
print(is_prime(2))  # True
print(is_prime(3))  # True
print(is_prime(5))  # True
print(is_prime(6))  # False
print(is_prime(7))  # True
print(is_prime(8))  # False
print(is_prime(9))  # False


# We can use the function is_prime to check if the length of a string is a prime number:

def prime_length_helper(num):
    if num % 2 == 0 and num > 2:  # If the number is even and not 2
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def prime_length(string):
    length =