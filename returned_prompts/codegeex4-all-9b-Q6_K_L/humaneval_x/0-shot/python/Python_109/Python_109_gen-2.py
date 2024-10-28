def move_one_ball(arr):
    if len(arr) == 0:
        return True
    arr.sort()
    for i in range(len(arr)):
        if arr == arr[i:] + arr[:i]:
            return True
    return False

print(move_one_ball([3, 4, 5, 1, 2])) # True
print(move_one_ball([3, 5, 4, 1, 2])) # False