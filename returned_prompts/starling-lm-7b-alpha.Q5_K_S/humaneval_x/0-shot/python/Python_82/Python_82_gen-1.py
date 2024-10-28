    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    length = len(string)
    return is_prime(length)








# Test cases
print(prime_length('Hello'))  # True
print(prime_length('abcdcba'))  # True
print(prime_length('kittens'))  # True
print(prime_length('orange'))  # False

# More test cases
print(prime_length('World'))  # True
print(prime_length('Apple'))  # False
print(prime_length('Mango'))  # True
print(prime_length('Banana'))  # False

```
