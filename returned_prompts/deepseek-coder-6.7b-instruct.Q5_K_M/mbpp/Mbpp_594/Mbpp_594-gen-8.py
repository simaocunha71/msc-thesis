def diff_even_odd(lst):
    first_even = next((i for i in lst if i % 2 == 0), None)
    first_odd = next((i for i in lst if i % 2 != 0), None)
    return first_even - first_odd if first_even and first_odd else None

print(diff_even_odd([1,3,5,7,4,1,6,8])) # 3

# Using List Comprehension
def diff_even_odd(lst):
    first_even = next((i for i in lst if i % 2 == 0), None)
    first_odd = next((i for i in lst if i % 2 != 0), None)
    return [first_even - first_odd] if first_even and first_odd else None

print(diff_even_odd([1,3,5,7,4,1,6,8])) # [3]
"""

