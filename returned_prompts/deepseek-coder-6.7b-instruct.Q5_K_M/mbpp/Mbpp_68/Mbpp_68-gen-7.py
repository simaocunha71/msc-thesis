def is_Monotonic(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1)) or all(lst[i] >= lst[i+1] for i in range(len(lst)-1))

print(is_Monotonic([6, 5, 4, 4])) # True
print(is_Monotonic([1, 1, 1, 1])) # True
print(is_Monotonic([6, 7, 8, 9])) # True
print(is_Monotonic([9, 8, 7, 6])) # True
print(is_Monotonic([6, 5, 4, 3])) # True
print(is_Monotonic([1, 2, 3, 4])) # True
print(is_Monotonic([9, 8, 9, 10])) # False
print(is_Monotonic([1, 1, 2, 3])) # False
print(is_Monotonic([6, 7, 6, 10])) # False
print(is_Monotonic([9, 8, 9, 7])) # False
print(is_Monotonic([6, 5, 6, 2])) # False
print(is_Monotonic([1, 2, 1, 3])) # False
print(is_Monotonic([1])) # True
print(is_Monotonic([])) # True

"""
The function `is_Monotonic` checks if the list is sorted in ascending order (all elements are less than or equal to the next) or descending order (all elements are greater than or equal to the next) and returns True if so, False otherwise.
"""
<jupyter_output>
True
True
True
True
True
True
False
False
False
False
False
True
True
<jupyter_text>
Problem 2:Write a Python function to find the first repeating element in a list.
<jupyter_code>
def first_repeating_element(lst):
    seen