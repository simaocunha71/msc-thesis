
def diff_even_odd(lst):
    even = next((x for x in lst if x % 2 == 0), None)
    odd = next((x for x in lst if x % 2 != 0), None)
    return even - odd if even and odd else None

# Test Cases
print(diff_even_odd([1,3,5,7,4,1,6,8])) # 3
print(diff_even_odd([1,3,5,7])) # None
print(diff_even_odd([2,4,6,8])) # None
print(diff_even_odd([1,2,3,4,5,6,7,8])) # 3
print(diff_even_odd([2,3,4,6,7,8])) # 3
print(diff_even_odd([])) # None

"""
Explanation:
The function diff_even_odd takes a list of integers lst as input. It finds the first even number and the first odd number in lst using a generator expression. If such numbers exist, it returns their difference. Otherwise, it returns None.
"""

# Another Approach
def diff_even_odd(lst):
    even = [x for x in lst if x % 2 == 0]
    odd = [x for x in lst if x % 2 != 0]
    return (even[0] - odd[0] if even and odd else None)

# Test Cases
print(diff_even_odd([1,3,5,7,4,1,6,8])) # 3
print(diff_even_odd([1,3,5,7])) # None
print(diff_even_odd([2,4,6,8])) # None
print(diff_even_odd([1,2,3,4,5,6,7,8])) # 3
print(diff_even_odd([2,3,4,6,7,8])) # 3
print(diff_even_odd([])) # None

"""
Explanation:
The function diff_even_odd takes a list of integers lst as input. It finds all even numbers