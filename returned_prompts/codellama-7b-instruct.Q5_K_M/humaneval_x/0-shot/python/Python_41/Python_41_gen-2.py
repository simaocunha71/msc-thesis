
    # Initialize variables
    left_to_right = [0] * n
    right_to_left = [0] * n
    total_collisions = 0

    # Loop through the cars
    for i in range(n):
        # Loop through the cars to the left of this one
        for j in range(i):
            # If this car is moving left to right
            if left_to_right[j]:
                # If the car to the left is moving right to left
                if right_to_left[i]:
                    # Increment the number of collisions
                    total_collisions += 1
        # Loop through the cars to the right of this one
        for j in range(i, n):
            # If this car is moving right to left
            if right_to_left[j]:
                # If the car to the right is moving left to right
                if left_to_right[i]:
                    # Increment the number of collisions
                    total_collisions += 1

    # Return the total number of collisions
    return total_collisions
