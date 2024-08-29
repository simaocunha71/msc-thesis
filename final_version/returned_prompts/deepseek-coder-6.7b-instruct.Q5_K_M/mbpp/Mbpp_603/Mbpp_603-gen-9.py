def get_ludic(n):
    ludic_numbers = []
    for i in range(1, n+1):
        if i & (i-1) == 0:
            ludic_numbers.append(i)
    return ludic_numbers

print(get_ludic(10))

"""
Explanation:
A number is lucid if it is a power of 2 or if the binary representation of a (x-1) is a lucid number.
For example, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, etc. are lucid numbers.
This function works by checking each number from 1 up to n to see if it's a lucid number or not.
"""
<jupyter_output>
[1, 2, 3, 5, 7]
<jupyter_text>
**Problem 2**Given an array of integers, write a function to return the indices of the two numbers such that they add up to a specific target.You may assume that each input would have exactly one solution, and you may not use the same element twice.
<jupyter_code>
