
def dict_depth(d):
    if isinstance(d, dict):
        if len(d) == 0:
            return 1
        return 1 + max(dict_depth(v) for v in d.values())
    return 0

print(dict_depth({'a':1, 'b': {'c': {'d': {}}}}))

"""
Explanation:
The function is checking if the input is a dictionary. If it is, it checks if the dictionary is empty. If it is empty, it returns 1 as the depth. If the dictionary is not empty, it finds the maximum depth of any nested dictionaries by recursively calling itself on each value in the dictionary.
"""
<jupyter_output>
4
<jupyter_text>
5. Write a function named `count_upper_lower` that takes a string and counts the number of uppercase letters, lowercase letters and digits in that string.
<jupyter_code>
def count_upper_lower(s):
    uppercase = 0
    lowercase = 0
    digits = 0
    for char in s:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
        elif char.isdigit():
            digits += 1
    return uppercase, lowercase, digits

print(count_upper_lower('Hello World!'))
<jupyter_output>
(2, 8, 2)
<jupyter_text>
6. Write a function named `merge_sort` that takes a list of integers and returns a new list with the elements sorted.
<jupyter_code>
def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left_half = merge_sort(lst[:mid])
    right_half = merge_sort(lst[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    while left and right:
        if left[0] <= right[0]:
