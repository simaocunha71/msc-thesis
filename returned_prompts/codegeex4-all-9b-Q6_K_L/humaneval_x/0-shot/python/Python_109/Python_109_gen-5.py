def move_one_ball(arr):
    if not arr:
        return True
    
    sorted_arr = sorted(arr)
    min_index = arr.index(min(arr))
    
    for i in range(min_index, len(arr)):
        if arr[i:] + arr[:i] == sorted_arr:
            return True
    
    return False

print(move_one_ball([3, 4, 5, 1, 2]))  # True
print(move_one_ball([3, 5, 4, 1, 2]))  # False