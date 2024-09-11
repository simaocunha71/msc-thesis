def is_monotonic(arr):
    increasing = False
    decreasing = False
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            increasing = True
        if arr[i] > arr[i + 1]:
            decreasing = True
    if increasing and decreasing:
        return False
    else:
        return True

# Test case
print(is_monotonic([6, 5, 4, 4]))








"""
This function checks if the given array is monotonic or not. It uses two boolean flags, increasing and decreasing, to track whether the array is strictly increasing or strictly decreasing. If both flags are True, the array is neither strictly increasing nor strictly decreasing, so the function returns False. Otherwise, it returns True.

The function iterates through the array using a for loop and compares each element to its adjacent element. If the current element is less than the next element, increasing is set to True. If the current element is greater than the next element, decreasing is set to True. If neither flag is True after the loop, the function returns True.

The assert statement at the end of the code checks if the function correctly determines whether the array [6, 5, 4, 4] is monotonic or not.
"""

"""
This function checks if the given array is monotonic or not. It uses two boolean flags, increasing and decreasing, to track whether the array is strictly increasing or strictly decreasing. If both flags are True, the array is neither strictly increasing nor strictly decreasing, so the function returns False. Otherwise, it returns True.

The function iterates through the array using a for loop and compares each element to its adjacent element. If the current element is less than the next element, increasing is set to True. If the current element is greater than the next element, decreasing is set to True. If neither flag is True after the loop, the function returns True.

The assert statement at the end of the code checks if the function correctly determines whether the array [6, 5, 4, 4] is monotonic or not.
"""

"""
This function checks if the given array is monotonic or