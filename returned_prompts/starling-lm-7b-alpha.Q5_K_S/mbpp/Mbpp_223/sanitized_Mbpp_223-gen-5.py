def is_majority(arr, length, element):
    left = 0
    right = length - 1
    while left < right:
        if element > arr[left]:
            left += 1
        elif element < arr[right]:
            right -= 1
        else:
            return True
    return left == right