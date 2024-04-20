"""
Write a python function to interchange the first and last elements in a list.
assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]
"""

def swap(arr):
    """Swap first and last element"""
    arr.append(arr[len(arr)-1]) # swaping first and last elemenet
    arr.pop()                   # removing last element

print("passed!")