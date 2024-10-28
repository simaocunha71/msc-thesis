def check_min_heap(arr):
    # base case
    if len(arr) == 0 or len(arr) == 1:
        return True

    # recursive case
    left = 2 * index + 1
    right = 2 * index + 2

    # if left child is not present or right child is not present or
    # left child is greater than the parent or right child is greater than the parent
    # then it is not a min heap
    if (left >= len(arr) or right >= len(arr) or arr[left] < arr[index] or arr[right] < arr[index]):
        return False

    # if the above conditions are not satisfied then recur for the left and right sub-tree
    return check_min_heap(arr[left:]) and check_min_heap(arr[right:])

    # time complexity is O(n), space complexity is O(n)


