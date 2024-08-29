
def last(lst, num):
    try:
        return len(lst) - 1 - lst[::-1].index(num)
    except ValueError:
        return -1

print(last([1, 2, 3], 1)) # 0

"""
Explanation:
The function works by reversing the list and finding the index of the number. This gives the index from the end of the list.
The length of the list is then subtracted from this index to give the position from the start of the list.
If the number is not in the list, the index function will throw a ValueError which is caught and -1 is returned.
"""

# Alternative solution
def last(lst, num):
    try:
        return lst[::-1].index(num)
    except ValueError:
        return -1

print(last([1, 2, 3], 1)) # 0

"""
Explanation:
The alternative function works in the same way, but it doesn't subtract the length of the list from the index.
This is because the index function already returns the index from the end of the list.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 3:
<jupyter_code>
