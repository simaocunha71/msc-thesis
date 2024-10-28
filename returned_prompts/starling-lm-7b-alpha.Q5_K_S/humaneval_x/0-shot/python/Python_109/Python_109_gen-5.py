    # Move all ball to the right
    for i in range(len(arr)-1, 0, -1):
        if arr[i] < arr[i-1]:
            return False
    # If all balls are on the right side, return True
    if len(arr) > 1:
        if arr[0] > arr[1]:
            return False
    return True

# Testing
print(move_one_ball([3, 4, 5, 1, 2]))  # True
print(move_one_ball([3, 5, 4, 1, 2]))  # False
print(move_one_ball([2, 3, 4, 5, 1]))  # True
print(move_one_ball([1, 1, 1, 2, 2]))  # True
print(move_one_ball([1]))  # True
print(move_one_ball([]))  # True
print(move_one_ball([1, 0]))  # False
print(move_one_ball([0, 1]))  # False
print(move_one_ball([1, 2, 3, 0]))  # True
print(move_one_ball([0, 2, 3, 1]))  # True
print(move_one_ball([1, 2, 3, 0]))  # True
print(move_one_ball([0, 2, 3, 1]))  # True
print(move_one_ball([0, 1, 2, 3]))  # False








































































































































