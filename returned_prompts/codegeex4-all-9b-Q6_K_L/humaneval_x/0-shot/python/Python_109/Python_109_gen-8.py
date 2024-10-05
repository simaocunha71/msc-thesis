def move_one_ball(arr):
    if len(arr) == 0:
        return True
    sorted_arr = sorted(arr)
    if sorted_arr == arr:
        return True
    for i in range(1, len(arr)):
        if arr[i:] + arr[:i] == sorted_arr:
            return True
    return False

print(move_one_ball([3, 4, 5, 1, 2]))
print(move_one_ball([3, 5, 4, 1, 2]))