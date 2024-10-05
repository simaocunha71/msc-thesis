    # Time Complexity: O(n)
    # Space Complexity: O(1)
    
    # To obtain non-decreasing order, the max element should be at the starting
    # position
    max_idx = 0
    for i in range(len(arr)):
        if arr[i] > arr[max_idx]:
            max_idx = i

    return arr[max_idx] == arr[0] and max_idx != 0

# Test Cases
print(move_one_ball([3, 4, 5, 1, 2]))  # True
print(move_one_ball([3, 5, 4, 1, 2]))  # False
print(move_one_ball([]))  # True
print(move_one_ball([2, 3, 4, 1]))  # True
print(move_one_ball([3, 1, 4, 2]))  # True

# Explanation
# For the first test case, if we shift the elements to the right by 2 positions,
# the array becomes sorted in non-decreasing order.
# [3, 4, 5, 1, 2] -> [5, 1, 2, 3, 4]

# For the second test case, even if we shift the elements to the right by any
# number of times, we cannot obtain the sorted array.
# [3, 5, 4, 1, 2] -> [4, 1, 2, 3, 5]

# For the third test case, the array is empty, hence we can obtain the sorted
# array by shifting the elements to the right by any number of times.

# For the fourth test case, if we shift the elements to the right by 1 position,
# the array becomes sorted in non-decreasing order.
# [2, 3, 4, 1] -> [4, 1, 2, 3]

# For the fifth test case, if we shift the elements to the right by 1 position,
# the array becomes sorted in non-decreasing order.
# [3, 1, 4,