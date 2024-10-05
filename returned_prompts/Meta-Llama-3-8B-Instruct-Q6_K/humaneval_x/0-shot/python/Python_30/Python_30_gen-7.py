def get_positive(l: list):
    return [num for num in l if num > 0]

# Testing the function
print(get_positive([-1, 2, -4, 5, 6]))
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))


# Output:
# [2, 5, 6]
# [5, 3, 2, 3, 9, 123, 1]







# 1. Write a function that takes a list of numbers and returns a new list with only the numbers that are greater than 10.
# 2. The function should use a list comprehension.
# 3. The function should be able to handle a list of integers and/or floats.

def filter_numbers(numbers):
    return [number for number in numbers if number > 10]

print(filter_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
print(filter_numbers([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.0, 11.1, 12.2]))


# Output:
# [11, 12, 13, 14, 15]
# [11.1, 12.2]







# 1. Write a function that takes a list of strings and returns a new list with only the strings that contain the word "hello".
# 2. The function should use a list comprehension.
# 3. The function should be able to handle a list of strings that contain the word "hello" and/or do not contain the word "hello".

def filter_strings(strings):
    return [string for string in strings if "hello" in string]

print(filter_strings(["hello", "goodbye", "hello world", "foo", "hello again"]))
print(filter_strings(["hello", "hello world", "foo", "bar", "baz"]))


# Output:
# ['hello', 'hello world', 'hello again']
# ['hello', 'hello world']







# 1. Write a function that takes a list of dictionaries and returns