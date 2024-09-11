"""
def pancake_sort(arr):
    for i in range(len(arr)):
        max_index = i
        for j in range(i+1, len(arr)):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr


def test_pancake_sort():
    assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]

test_pancake_sort()
"""

def pancake_sort(arr):
    for i in range(len(arr)):
        max_index = i
        for j in range(i+1, len(arr)):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[:i+1], arr[max_index:i+1] = arr[max_index:i+1], arr[:i+1]
    return arr

def test_pancake_sort():
    assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]

test_pancake_sort()


"""
In the original solution, swapping values in the array is done with
arr[i], arr[max_index] = arr[max_index], arr[i]
However, this line of code is incorrect as it only swaps the pointers of the variables, but the values remain the same.
To correctly swap the values, we should use the following syntax:
arr[:i+1], arr[max_index:i+1] = arr[max_index:i+1], arr[:i+1]
"""


"""
In the original solution, the outer for loop iterates over the indices of the array, and the inner for loop finds the index of the maximum value in the remaining part of the array.
However, this approach is incorrect as it