def first_odd(numbers):
    for num in numbers:
        if num % 2 != 0:
            return num
    return None

print(first_odd([1,3,5])) # 1

# Find the first even number in a given list of numbers.
# assert first_even([1,2,3]) == 2

def first_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            return num
    return None

print(first_even([1,2,3])) # 2

# Find the first number which is divisible by 3 in a given list of numbers.
# assert first_divisible_by_3([1,2,3]) == 3

def first_divisible_by_3(numbers):
    for num in numbers:
        if num % 3 == 0:
            return num
    return None

print(first_divisible_by_3([1,2,3])) # 3

# Find the first number which is divisible by 5 in a given list of numbers.
# assert first_divisible_by_5([1,5]) == 5

def first_divisible_by_5(numbers):
    for num in numbers:
        if num % 5 == 0:
            return num
    return None

print(first_divisible_by_5([1,5])) # 5

# Find the first number which is divisible by 7 in a given list of numbers.
# assert first_divisible_by_7([1,7]) == 7

def first_divisible_by_7(numbers):
    for num in numbers:
        if num % 7 == 0:
            return num
    return None

print(first_divisible_by_7([1,7])) # 7

# Find the first number which is divisible by both 3 and 5 in a given list of numbers.
# assert first_divisible_by_3_and_5([1,15]) == 15

def first_divisible_by_3_and_5(numbers):
    for num in numbers:
        if