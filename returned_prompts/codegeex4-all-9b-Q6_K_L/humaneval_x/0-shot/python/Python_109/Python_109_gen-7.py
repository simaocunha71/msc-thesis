def move_one_ball(arr):
    if len(arr) <= 1:
        return True
    for i in range(len(arr)):
        arr = arr[-1:] + arr[:-1]
        if arr == sorted(arr):
            return True
    return False

# Testing the function
print(move_one_ball([3, 4, 5, 1, 2]))  # True
print(move_one_ball([3, 5, 4, 1, 2]))  # False