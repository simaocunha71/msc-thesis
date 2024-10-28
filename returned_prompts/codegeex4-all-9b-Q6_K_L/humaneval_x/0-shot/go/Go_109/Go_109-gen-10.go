def move_one_ball(arr):
    # If the array is empty, return True
    if not arr:
        return True

    # Sort the array
    sorted_arr = sorted(arr)

    # Check if the array can be sorted by performing right shift operations
    for i in range(len(arr)):
        # Perform a right shift operation
        shifted_arr = arr[-i:] + arr[:-i]

        # Check if the shifted array is sorted
        if shifted_arr == sorted_arr:
            return True

    # If none of the shifted arrays are sorted, return False
    return False

# Test cases
print(move_one_ball([3, 4, 5, 1, 2]))  # True
print(move_one_ball([3, 5, 4, 1, 2]))  # False

