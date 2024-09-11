Shell Sort

shell_sort(arr):
    # Set the initial gap to the length of the array divided by 2
    gap = len(arr) // 2

    # Iterate over the array starting from the first element
    while gap > 0:
        # Iterate over the array starting from the gap's position
        for i in range(gap, len(arr)):
            # Store the current element in a temporary variable
            temp = arr[i]

            # Swap the current element with its previous element until the gap's position is reached
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            # Insert the temporary element at its correct position
            arr[j] = temp

        # Reduce the gap by dividing it by 2
        gap //= 2

    # Return the sorted array
    return arr

# Test the function with the given array
assert shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]) == [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]

"""
The shell_sort function implements the Shell sort algorithm to sort the given array in ascending order. It uses the gap variable to define the initial gap between elements that are compared. The algorithm starts by comparing elements that are gap positions apart and gradually reduces the gap until it reaches the minimum gap of 1. The function iterates over the array, swapping elements if they are out of order, until the entire array is sorted. Finally, it returns the sorted array.

The assert statement checks if the function correctly sorts the given array [12, 23, 4, 5, 3, 2, 12, 81, 56, 95] and verifies that the result is [2, 3, 4, 5, 12, 12, 23, 56, 81, 95].
"""

# Python3 program