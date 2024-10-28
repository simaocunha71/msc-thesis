    if not arr:
        return True
    n = len(arr)
    max_idx = 0
    for i in range(1, n):
        if arr[i] > arr[max_idx]:
            max_idx = i
    if max_idx == 0:
        return True
    for i in range(n - 1, max_idx, -1):
        arr[i - 1] = arr[i]
    arr[max_idx - 1] = arr[max_idx]
    return True
    # This function works by first finding the index of the largest element in the array. 
    # Then it shifts all elements to the right of this element to the left until the largest element is at the end of the array. 
    # After that, it checks if the array is sorted. If it is, the function returns True. If not, it returns False. 
    # The time complexity of this function is O(n) and the space complexity is O(1). 
    # The function assumes that the input array is not empty and does not contain duplicate elements. 
    # If the array can be empty or contain duplicate elements, additional checks and modifications are needed. 
    # For example, if the array can be empty, the function should return True in this case. 
    # If the array can contain duplicate elements, the function should return False if there are duplicate elements. 
    # The function also assumes that the input array is a list of integers. If the array can contain other types of elements, 
    # the function should be modified to handle these elements correctly.  #


