def left_insertion(lst, val):
    for i in range(len(lst)):
        if lst[i] >= val:
            return i
    return len(lst)

print(left_insertion([1,2,4,5],6)) # 4

"""
Explanation:
The function loops through the list. When it finds a number in the list that is bigger or equal to the given value, it returns the current index. If the given value is bigger than all numbers in the list, it returns the length of the list (as it should be inserted at the end).
"""

"""
