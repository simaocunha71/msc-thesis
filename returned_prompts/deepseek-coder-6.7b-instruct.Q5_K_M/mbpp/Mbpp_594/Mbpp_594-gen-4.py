def diff_even_odd(lst):
    first_even = next((i for i in lst if i % 2 == 0), None)
    first_odd = next((i for i in lst if i % 2 != 0), None)
    return first_even - first_odd if first_even and first_odd else None

print(diff_even_odd([1,3,5,7,4,1,6,8]))  # 3

# Alternatively, using list comprehension:
def diff_even_odd_v2(lst):
    first_even = next((i for i in lst if i % 2 == 0), None)
    first_odd = next((i for i in lst if i % 2 != 0), None)
    return [first_even - first_odd] if first_even and first_odd else None

print(diff_even_odd_v2([1,3,5,7,4,1,6,8]))  # [3]

"""
The function diff_even_odd first finds the first even and odd number in the list using the next function. 
The next function returns the first item in the list that matches the condition, and None if no item matches the condition.
The difference between these two numbers is returned. If either the first even or odd number does not exist in the list, None is returned.
"""

# Alternatively, using list comprehension:
def diff_even_odd_v2(lst):
    first_even = next((i for i in lst if i % 2 == 0), None)
    first_odd = next((i for i in lst if i % 2 != 0), None)
    return [first_even - first_odd] if first_even and first_odd else None

print(diff_even_odd_v2([1,3,5,7,4,1,6,8]))  # [3]

"""
The function diff_even_odd first finds the first even and odd number in the list using the next function. 
The next function returns the first item in the list that matches the condition, and None if no item matches the condition.
The difference between these two