def move_one_ball(arr):
    if len(arr) == 0:
        return True
    min_value = min(arr)
    min_index = arr.index(min_value)
    arr = arr[min_index:] + arr[:min_index]
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

print(move_one_ball([3, 4, 5, 1, 2])) # True
print(move_one_ball([3, 5, 4, 1, 2])) # False