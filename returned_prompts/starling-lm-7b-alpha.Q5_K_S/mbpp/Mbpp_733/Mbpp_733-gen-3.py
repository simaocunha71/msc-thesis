def find_first_occurrence(arr, num):
    """
    Find the index of the first occurrence of a given number in a sorted array.

    Parameters:
    arr (list): The sorted array.
    num (int): The number to find.

    Returns:
    int: The index of the first occurrence of the number.
    """
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return -1

# Example usage
print(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5))  # Output: 1

"""
This function takes in a sorted array and a number, and iterates through the array using a for loop. It checks if each element is equal to the given number, and if so, returns the index of that element. If no such element is found, it returns -1. In the example usage, the function is called with the array [2, 5, 5, 5, 6, 6, 8, 9, 9, 9] and the number 5, and it correctly returns 1, as the first occurrence of 5 in the array is at index 1.
"""

```
  
# In this code, we define a function called `find_first_occurrence` that takes in two parameters: `arr` (the sorted array) and `num` (the number to find). 

The function uses a `for` loop to iterate through each element in the array. Inside the loop, it checks if the current element is equal to the given number using the `==` operator. If it is, the function immediately returns the index of that element using the `return` keyword. 

If the loop completes without finding a match, the function returns -1 to indicate that the number was not found in the array. 

In the example usage provided, the function is called with the array `[2, 5, 5, 5, 6, 6, 8, 9, 9, 9]` and the number `5`. The function correctly returns 1, as the first occur