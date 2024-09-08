def check_greater(arr, num):
    for i in arr:
        if i <= num:
            return False
    return True

print(check_greater([1, 2, 3, 4, 5], 4))  # False
print(check_greater([1, 2, 3, 4, 5], 6))  # True

"""
Write a function that takes a list of integers and returns the sum of the integers.
assert sum_list([1, 2, 3, 4, 5]) == 15
"""

def sum_list(numbers):
    return sum(numbers)

print(sum_list([1, 2, 3, 4, 5]))  # 15

"""
Write a function that takes a list of integers and returns a new list with all the even numbers from the original list.
assert filter_even([1, 2, 3, 4, 5]) == [2, 4]
"""

def filter_even(numbers):
    return [n for n in numbers if n % 2 == 0]

print(filter_even([1, 2, 3, 4, 5]))  # [2, 4]

"""
Write a function that takes a list of integers and returns the maximum number from the list.
assert max_num([1, 2, 3, 4, 5]) == 5
"""

def max_num(numbers):
    return max(numbers)

print(max_num([1, 2, 3, 4, 5]))  # 5

"""
Write a function that takes a string and returns a new string with all the vowels replaced with a '*'.
assert replace_vowels('hello world') == 'h*llo w*rld'
"""

def replace_vowels(s):
    return ''.join('*' if c.lower() in 'aeiou' else c for c in s)

print(replace_vowels('hello world'))  # 'h*llo w*rld'

"""
Write a function that takes a string and returns a