def is_majority(arr, n, elem):
    # Write your code here
    left = 0
    right = n-1
    while left < right:
        if arr[left] == elem:
            left += 1
        elif arr[right] == elem:
            right -= 1
        elif elem > arr[left] and elem < arr[right]:
            break
        elif elem >= arr[left] and elem <= arr[right]:
            left = right
        else:
            right = left
    return right == n-1