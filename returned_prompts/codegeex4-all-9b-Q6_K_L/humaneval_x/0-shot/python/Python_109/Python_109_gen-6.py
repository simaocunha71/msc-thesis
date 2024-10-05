def move_one_ball(arr):
    if not arr:
        return True
    
    arr.sort()
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            return False
    return True

# Test cases
print(move_one_ball([3, 4, 5, 1, 2]))  # True
print(move_one_ball([3, 5, 4, 1, 2]))  # False