def is_sublist(arr, subarr):
    # Check if the length of the sublist is greater than the length of the list
    if len(subarr) > len(arr):
        return False
    # Traverse the list
    for i in range(len(arr)):
        # If the sublist is found, return True
        if arr[i:i+len(subarr)] == subarr:
            return True
    # If the sublist is not found, return False
    return False

# Test the function
print(is_sublist([2,4,3,5,7], [3,7])) # Output: True
print(is_sublist([2,4,3,5,7], [3,7,8])) # Output: False




"""
A sublist is a contiguous sequence of elements within a list. For example, the sublist [3,7] is a sublist of [2,4,3,5,7].
The function checks whether the given sublist is present in the list by using a simple loop to traverse through the list.
If the sublist is found, the function returns True; otherwise, it returns False.
"""




















"""
A sublist is a sequence of elements that appear in a list in a contiguous order. For example, the sublist [3, 7] is a sublist of the list [2, 4, 3, 5, 7].
To check if a list contains a given sublist, you can use a simple loop to traverse through the list and check if the sublist appears in the list.
If the sublist is found in the list, the function returns True; otherwise, it returns False.
"""


"""
A sublist is a contiguous sequence of elements within a list. For example, the sublist [3, 7] is a sublist of [2, 4, 3, 5, 7].
To check if a list contains a given sublist, you can use a simple loop to traverse through the list and compare each subsequence of elements with the sublist.
If the sublist is found in the list, the function returns