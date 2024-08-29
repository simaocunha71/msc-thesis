def is_Monotonic(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1)) or all(lst[i] >= lst[i+1] for i in range(len(lst)-1))

print(is_Monotonic([6, 5, 4, 4]))  # True

"""
This function works by checking whether all elements in the list are less than or equal to the next element, or all elements are greater than or equal to the next. If either of these conditions is met, it returns True, otherwise it returns False.
"""

"""
The time complexity of this function is O(n), where n is the length of the list. This is because it needs to iterate over every element in the list once.
"""

"""
The space complexity of this function is O(1), because it only uses a constant amount of space to store the list and the two comparison results.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2
<jupyter_code>
"""
