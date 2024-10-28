def move_one_ball(arr):
    # If the array is empty, return True
    if not arr:
        return True
    
    # Sort the array and store it in a new variable
    sorted_arr = sorted(arr)
    
    # Iterate through the array
    for i in range(len(arr)):
        # Perform a right shift operation
        arr = arr[-1:] + arr[:-1]
        
        # Check if the array is sorted
        if arr == sorted_arr:
            return True
    
    # If the array is not sorted after any number of shifts, return False
    return False

# Test cases
print(move_one_ball([3, 4, 5, 1, 2]))  # True
print(move_one_ball([3, 5, 4, 1, 2]))  # False
print(move_one_ball([]))               # True

