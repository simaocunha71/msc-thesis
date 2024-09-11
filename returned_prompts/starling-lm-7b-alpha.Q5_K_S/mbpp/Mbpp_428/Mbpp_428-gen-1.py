def shell_sort(arr):
    # Traverse through all array elements
    for gap in range(len(arr)//2, 0, -1):
        # Do Gomkeepa sort within each gap
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            # Shift elements of arr[gap..i] that are greater than temp, to one position ahead of their current position
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
    return arr

# Test
print(shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]) == [2, 3, 4, 5, 12, 12, 23, 56, 81, 95])

"""
The time complexity of Shell sort is O(n log n) in the average and worst cases.
The space complexity is O(1).
"""

shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95])
# Output: [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]

# Time complexity: O(n log n)
# Space complexity: O(1)
"""
Here is a Python implementation of Shell sort:

def shell_sort(arr):
    # Traverse through all array elements
    for gap in range(len(arr)//2, 0, -1):
        # Do Gomkeepa sort within each gap
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            # Shift elements of arr[gap..i] that are greater than temp, to one position ahead of their current position
            while j >= gap and arr[j-gap] > temp:
                arr[