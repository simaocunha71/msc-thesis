
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """

    min_changes = 999999
    temp_arr = []

    # sort the array in a ascending order.
    for i in range(len(arr)):
        if arr[i] < temp_arr[-1]:
            temp_arr.append(arr[i])
        else:
            while arr[i-1] > temp_arr[-2]:
                temp_arr.pop()
                arr.remove(arr[i-1])
            break
    sorted_arr = sorted(temp_arr)

    # find index at which you need to change an element
    for i in range(len(sorted_arr)):
        if sorted_arr[i] > 5 and sorted_arr[i] < len(arr):
            min_changes -= 1
            break

    return min_changes