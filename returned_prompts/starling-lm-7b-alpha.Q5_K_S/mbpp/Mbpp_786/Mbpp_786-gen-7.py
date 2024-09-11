def right_insertion(arr, value):
    # Write your code here
    for i in range(len(arr)):
        if value < arr[i]:
            return i
    return len(arr)

"""
The time complexity of this function is O(n) where n is the length of the list.
"""


# Testing the function
print(right_insertion([1, 2, 4, 5], 6))
print(right_insertion([1, 2, 3, 4, 5, 6, 7], 8))
print(right_insertion([1, 2, 3, 4, 5, 6, 7], 0))
print(right_insertion([], 0))
print(right_insertion([1, 2, 3, 4, 5, 6, 7], 7))



"""
The function right_insertion is a function that takes in an array and a value as arguments. The function iterates through the array and checks if the value is less than the current element in the array. If the value is less, it returns the index of the current element. If the value is not less than any of the elements in the array, it returns the length of the array. The time complexity of the function is O(n) where n is the length of the array.
"""

```

```