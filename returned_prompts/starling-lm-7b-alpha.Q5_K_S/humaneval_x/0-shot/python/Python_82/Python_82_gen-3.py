
def prime_length(string):
    if len(string) == 1:
        return True
    for i in range(2, len(string)):
        if len(string) % i == 0:
            return False
    return True


# Testing the function
print(prime_length('Hello'))  # True
print(prime_length('abcdcba'))  # True
print(prime_length('kittens'))  # True
print(prime_length('orange'))  # False








```