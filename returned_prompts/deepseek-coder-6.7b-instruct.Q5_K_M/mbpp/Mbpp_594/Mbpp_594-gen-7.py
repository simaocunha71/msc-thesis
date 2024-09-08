def diff_even_odd(lst):
    even_num = next((x for x in lst if x % 2 == 0), None)
    odd_num = next((x for x in lst if x % 2 != 0), None)
    return even_num - odd_num if even_num and odd_num else None

assert diff_even_odd([1,3,5,7,4,1,6,8])==3
"""
In the above function, we're using python's built-in next() function to get the first even and odd number from the list. If no even or odd number is found, None is returned. The difference between these two numbers is then returned.
"""

# 2.

