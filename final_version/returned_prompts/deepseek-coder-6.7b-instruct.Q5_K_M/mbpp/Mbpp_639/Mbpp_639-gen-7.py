def sample_nam(names):
    total_length = 0
    for name in names:
        if name[0].isupper():
            total_length += len(name)
    return total_length

print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']))  # Output: 16


# Q2:
"""
Write a function that takes an integer as a parameter and returns True if the number is a prime number, and False otherwise.
"""

A2:
def is_prime(n):
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

print(is_prime(7))  # Output: True
print(is_prime(10))  # Output: False


# Q3:
"""
Write a function that takes a string as a parameter and returns a dictionary with the frequency of each character in the string.
"""

A3:
def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

print(char_frequency('google.com'))  # Output: {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}


# Q4:
"""
Write a function that takes a list of integers as a parameter and returns the sum of all the integers in the list.
"""

A4:
def sum_list(nums):
    return sum(nums)

print(sum_list([1, 2, 3, 4, 5]))  # Output: 15


# Q5:
"""