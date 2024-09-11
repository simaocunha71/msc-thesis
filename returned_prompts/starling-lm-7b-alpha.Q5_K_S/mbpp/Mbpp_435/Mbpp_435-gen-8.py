def last_Digit(num):
    if num < 0:
        return 0
    while num >= 10:
        num = num // 10
    return num % 10



# Assert
assert last_Digit(123) == 3

"""
Write a python function to check if the given number is prime.
assert isPrime(3) == True
"""

def isPrime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

# Assert
assert isPrime(3) == True

"""
Write a python function to get the first common element from the given two sorted arrays.
assert firstCommonElement(array1, array2) == 2
"""

def firstCommonElement(array1, array2):
    i = 0
    j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] == array2[j]:
            return array1[i]
        elif array1[i] < array2[j]:
            i += 1
        else:
            j += 1
    return -1

# Assert
assert firstCommonElement([1, 2, 3, 4, 5], [2, 3, 4, 5, 6]) == 2

"""
Write a python function to calculate the factorial of a given number.
assert factorial(5) == 120
"""

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

# Assert
assert factorial(5) == 120

"""
Write a python function to calculate the sum of all the digits of a given number.
assert sum_of_digits(123) == 6
"""

def sum_of