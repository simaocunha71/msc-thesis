    # We will take the last element of the array and start moving it to the
    # starting position of the array and check if the array gets sorted or not.
    # If the array gets sorted then return True else return False.
    # Time Complexity: O(N)
    # Space Complexity: O(1)
    
    # Step 1: Initialize the variable 'index' with 0 and 'prev' with the value
    # of the first element of the array.

    index = 0
    prev = arr[index]

    # Step 2: Iterate over the array from index 1 to N-1.

    for i in range(1, len(arr)):

        # Step 3: Check if the current element of the array is greater than
        # the previous element of the array. If yes, then increment the
        # variable 'index' with 1 and update the value of the variable
        # 'prev' with the current element of the array. Else, return False.

        if arr[i] > prev:
            index += 1
            prev = arr[index]

        # Step 4: Check if the variable 'index' is equal to N-1. If yes,
        # then return True. Else, continue to the next iteration.

        if index == len(arr) - 1:
            return True

    # Step 5: If the variable 'index' is not equal to N-1, then return False.

    return False

# Driver's Code:
arr = [3, 4, 5, 1, 2]
print(move_one_ball(arr))

arr = [3, 5, 4, 1, 2]
print(move_one_ball(arr))

arr = [3, 4, 6, 5, 1, 2]
print(move_one_ball(arr))

arr = []
print(move_one_ball(arr))

















































