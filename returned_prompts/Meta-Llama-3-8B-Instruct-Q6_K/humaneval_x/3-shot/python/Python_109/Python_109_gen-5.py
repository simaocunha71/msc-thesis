    if not arr:
        return True

    i = 0
    while i < len(arr) - 1:
        if arr[i] > arr[i + 1]:
            return False
        i += 1

    return True
# This solution iterates over the array and checks if the current element is greater than the next one. If it is, the function returns False, indicating that it's not possible to sort the array by shifting elements to the right. If the function finishes iterating over the array without finding any such pair of elements, it returns True, indicating that it is possible to sort the array by shifting elements to the right. If the array is empty, the function returns True. 

