"""
def sequential_search(arr, element):
    bool = False
    index = -1
    for i in range(len(arr)):
        if arr[i] == element:
            bool = True
            index = i
    return (bool, index)

assert sequential_search([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)
"""

def sequential_search(arr, element):
    bool = False
    index = -1
    for i in range(len(arr)):
        if arr[i] == element:
            bool = True
            index = i
    return (bool, index)

assert sequential_search([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)

# This code uses a for loop to iterate through the array. It checks if the current element is equal to the element being searched for. If it is, it sets the boolean to True and the index to the current index. If it is not, it continues the loop until the end of the array is reached. Finally, it returns a tuple containing the boolean and the index.

# The time complexity of this code is O(n), where n is the length of the array. This is because the code needs to check each element in the array once to determine if it is present. 

# The space complexity of this code is O(1), meaning it uses a constant amount of space regardless of the size of the input array. This is because the code only uses a few variables to store the boolean and index values, and does not create any additional data structures. 

# This code can be used to efficiently search for an element in an array. However, it may not be the most efficient method for large arrays, as it requires iterating through the entire array to find the element. 

# The assert statement at the end of the code checks if the function correctly returns True and the index of the element when given the array [11,23,58,31,56,77,43,12,65,19