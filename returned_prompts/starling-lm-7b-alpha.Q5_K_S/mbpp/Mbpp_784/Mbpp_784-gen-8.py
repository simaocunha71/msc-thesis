def mul_even_odd(list):
    evens = []
    odds = []
    for i in range(len(list)):
        if i % 2 == 0:
            evens.append(list[i])
        else:
            odds.append(list[i])
    return evens[0] * odds[0]

# Python program to find the first even and odd number of the given
# list and returns the product of the same.
def mul_even_odd(list):
    evens = []
    odds = []
    # To store the first even and odd number in the given list.
    first_even = -1
    first_odd = -1
    for i in range(len(list)):
        if i % 2 == 0:
            evens.append(list[i])
            if first_even == -1:
                first_even = list[i]
        else:
            odds.append(list[i])
            if first_odd == -1:
                first_odd = list[i]
    # To return the product of the first even and odd number.
    return first_even * first_odd

# Driver code
list = [1,3,5,7,4,1,6,8]
print(mul_even_odd(list))

# This code is contributed by 
# Shubham Singh(SHUBHAM SINGH)







"""
Given a list of integers, find the product of the first even and odd number of the given list.

Examples:

mul_even_odd([1, 3, 5, 7, 4, 1, 6, 8]) ➞ 4

mul_even_odd([7, 4, 1, 6]) ➞ 28
"""

def mul_even_odd(list):
    evens = []
    odds = []
    for i in range(len(list)):
        if i % 2 == 0:
            evens.append(list[i])
        else:
            odds.append(list[i])
    return evens[