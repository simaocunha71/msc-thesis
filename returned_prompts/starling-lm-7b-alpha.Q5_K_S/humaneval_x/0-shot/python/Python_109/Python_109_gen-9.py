    # Find the maximum in the array
    max_val = max(arr)
    
    # Find the index of the maximum value in the array
    max_index = arr.index(max_val)
    
    # If the max_index is 0, return True
    if max_index == 0:
        return True
    
    # If the max_index is not 0, then find the 
    # index of the second maximum value in the array
    second_max = max(arr[0:max_index])
    
    # If the second maximum is less than the maximum, return True
    if second_max < max_val:
        return True
    
    # Else return False
    return False

# Driver code
arr = [3, 4, 5, 1, 2]
print(move_one_ball(arr))




```

This code implements a function `move_one_ball` that takes an array `arr` as input and checks if it is possible to obtain a sorted array by performing right shift operations. The function first finds the maximum value in the array and its index. If the index of the maximum value is 0, it means that the array is already sorted, so the function returns True. Otherwise, the function finds the index of the second maximum value in the array. If the second maximum value is less than the maximum value, it is possible to obtain a sorted array by performing right shift operations, so the function returns True. Otherwise, the function returns False.

In the given example, the array `[3, 4, 5, 1, 2]` is passed to the `move_one_ball` function, and the function returns True because it is possible to obtain a sorted array by performing two right shift operations: `[5, 4, 3, 2, 1]`.

The time complexity of this solution is O(n), where n is the length of the array. The space complexity is O(1), as no additional space is used.

Note: The solution assumes that the array `arr` is non-empty. If the array is empty, the function will return True, as it is trivially possible to obtain a sorted array by shifting all elements to the starting position.

