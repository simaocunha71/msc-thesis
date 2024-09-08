def last(lst, num):
    idx = len(lst) - 1
    while idx >= 0:
        if lst[idx] == num:
            return idx
        idx -= 1
    return -1

print(last([1,2,3],1)) # 0
"""
Explanation:
The function starts at the end of the list (last index) and works its way to the beginning. 
If it finds the number it's looking for, it returns the index. If it gets through the whole list without finding the number, it returns -1.
"""

def last(lst, num):
    try:
        return len(lst) - 1 - lst[::-1].index(num)
    except ValueError:
        return -1

print(last([1,2,3],1)) # 0
"""
Explanation:
The function uses the index method of the reversed list to get the index of the last occurrence of the number in the original list. 
It subtracts this from the length of the list minus one (to convert from 0-indexed to 1-indexed) and returns the result. 
If the number is not in the list, the index method will raise a ValueError which the function catches and returns -1.
"""

def last(lst, num):
    return len(lst) - 1 - lst[::-1].index(num) if num in lst else -1

print(last([1,2,3],1)) # 0
"""
Explanation:
The function uses the index method of the reversed list to get the index of the last occurrence of the number in the original list. 
It subtracts this from the length of the list minus one (to convert from 0-indexed to 1-indexed) and returns the result. 
If the number is not in the list, the function returns -1.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
