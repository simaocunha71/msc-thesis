def move_one_ball(arr):
    if not arr:
        return True

    min_idx = arr.index(min(arr))
    arr = arr[min_idx:] + arr[:min_idx]

    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False

    return True

print(move_one_ball([3, 4, 5, 1, 2]))
print(move_one_ball([3, 5, 4, 1, 2]))