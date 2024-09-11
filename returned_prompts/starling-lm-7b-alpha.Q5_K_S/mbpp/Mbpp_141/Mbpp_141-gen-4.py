"""
def pancake_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        max_val = max(arr)
        max_index = arr.index(max_val)
        max_val_index = arr.index(max_val)
        arr[max_index], arr[max_val_index] = arr[max_val_index], arr[max_index]
        pancake_sort(arr[:max_index])
        pancake_sort(arr[max_index+1:])
    return arr
"""

def pancake_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        max_val = max(arr)
        max_index = arr.index(max_val)
        pancake_sort(arr[:max_index])
        pancake_sort(arr[max_index:])
        arr[max_index], arr[0] = arr[0], arr[max_index]
    return arr


pancake_sort([15, 79, 25, 38, 69])

"""
Explanation:
This is a recursive function to sort a list of elements in ascending order using the Pancake sort algorithm.
The Pancake sort algorithm works by repeatedly flipping the first half of the array and sorting the array in place.
In this implementation, the function checks if the length of the array is 1, in which case it returns the array as it is already sorted.
Otherwise, it finds the maximum value in the array and its index, then swaps the values at the maximum index and the first index of the array.
Finally, it recursively calls the function on the first half and the second half of the array, until the entire array is sorted.
"""

# Python3 program to implement Pancake sort

def pancakeSort(arr, n):

    if (n == 1):
        return arr
    else:
        max_index = arr.index(max(arr))
        arr[max_index], arr[0] = arr[0], arr[max_index]
        p