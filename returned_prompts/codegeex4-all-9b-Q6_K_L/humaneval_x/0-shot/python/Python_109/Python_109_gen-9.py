def move_one_ball(arr):
    if len(arr) == 0: return True
    arr.sort()
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

print(move_one_ball([3, 4, 5, 1, 2])) # True
print(move_one_ball([3, 5, 4, 1, 2])) # False
print(move_one_ball([])) # True