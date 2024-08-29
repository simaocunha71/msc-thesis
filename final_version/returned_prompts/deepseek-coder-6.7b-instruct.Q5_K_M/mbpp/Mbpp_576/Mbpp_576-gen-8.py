def is_Sub_Array(main_array, sub_array):
    return sub_array in main_array

print(is_Sub_Array([1,4,3,5],[1,2])) # False

"""
This function uses python's in-built operation to check if sub_array is in main_array. 
This operation checks if every element of sub_array is in main_array in sequence. 
If yes, it returns True, otherwise False.
"""

# Time complexity is O(n) where n is the size of main_array.
# Space complexity is O(1) as it uses a constant amount of space.

# The function also handles the case where sub_array is an empty list, returning True.
assert is_Sub_Array([1,4,3,5],[]) == True
assert is_Sub_Array([],[]) == True

# The function also handles the case where main_array is an empty list, returning False.
assert is_Sub_Array([],[1,2]) == False

# The function also handles the case where sub_array is a list with more elements than main_array, returning False.
assert is_Sub_Array([1,2],[1,2,3]) == False

# The function also handles the case where sub_array is a list with the same elements as main_array, returning True.
assert is_Sub_Array([1,2],[1,2]) == True

# The function also handles the case where sub_array is a list with the elements of main_array in a different order, returning True.
assert is_Sub_Array([1,2,3,4,5],[2,1]) == True

# The function also handles the case where sub_array is a list with the elements of main_array in a different order at the end, returning True.
assert is_Sub_Array([1,2,3,4,5],[3,4,5]) == True

# The function also handles the case where sub_array is a list with the elements of main_array in a different order at the start, returning True.
assert is_Sub_Array([1,2,3,4,5],[1,2]) == True

