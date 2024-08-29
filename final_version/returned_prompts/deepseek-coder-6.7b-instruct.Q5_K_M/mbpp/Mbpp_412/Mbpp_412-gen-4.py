def remove_odd(numbers):
    return [number for number in numbers if number % 2 == 0]

print(remove_odd([1,2,3]))


"""
Write a python function to remove even numbers from a given list.
assert remove_even([1,2,3]) == [1,3]
"""

def remove_even(numbers):
    return [number for number in numbers if number % 2 != 0]

print(remove_even([1,2,3]))

"""
Write a python function to remove duplicates from a given list.
assert remove_duplicates([1,2,2,3,3,4]) == [1,2,3,4]
"""

def remove_duplicates(numbers):
    return list(set(numbers))

print(remove_duplicates([1,2,2,3,3,4]))

"""
Write a python function to remove all occurrences of a given element from a given list.
assert remove_all_occurrences(1,[1,2,1,3,1]) == [2,3]
"""

def remove_all_occurrences(element, numbers):
    return [number for number in numbers if number != element]

print(remove_all_occurrences(1,[1,2,1,3,1]))

"""
Write a python function to check if a given list is a palindrome.
assert is_palindrome([1,2,2,1]) == True
"""

def is_palindrome(numbers):
    return numbers == numbers[::-1]

print(is_palindrome([1,2,2,1]))

"""
Write a python function to reverse a given list.
assert reverse_list([1,2,3,4]) == [4,3,2,1]
"""

def reverse_list(numbers):
    return numbers[::-1]

print(reverse_list([1,2,3,4]))

"""
Write a python function to sort a given list in ascending order.
assert sort_list([4,2,3,1]) ==