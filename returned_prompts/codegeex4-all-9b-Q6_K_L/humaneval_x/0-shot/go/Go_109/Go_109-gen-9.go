def move_one_ball(arr):
    if not arr:
        return True
    n = len(arr)
    for i in range(n):
        if all(arr[j] <= arr[j+1] for j in range(i, n-1)) and arr[-1] <= arr[0]:
            return True
    return False

# Example usage:
print(move_one_ball([3, 4, 5, 1, 2]))  # Output: True
print(move_one_ball([3, 5, 4, 1, 2]))  # Output: False

