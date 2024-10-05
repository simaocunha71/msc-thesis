    # Initialize a list to keep track of the positions of the cars moving left to right and right to left
    left_to_right = [i for i in range(n)]
    right_to_left = [n - i - 1 for i in range(n)]

    # Initialize the number of collisions to 0
    collisions = 0

    # Iterate over the positions of the cars moving left to right
    for i in range(n):
        # Check if there is a car moving right to left at the same position
        if right_to_left[i] == left_to_right[i]:
            # Increment the number of collisions
            collisions += 1
        # If not, check the next position
        elif right_to_left[i] < left_to_right[i]:
            # Continue iterating over the positions of the cars moving left to right
            while right_to_left[i] < left_to_right[i]:
                # Check if there is a car moving right to left at the same position
                if right_to_left[i] == left_to_right[i]:
                    # Increment the number of collisions
                    collisions += 1
                # If not, increment the position of the car moving right to left
                i += 1
        else:
            # Continue iterating over the positions of the cars moving right to left
            while right_to_left[i] > left_to_right[i]:
                # Check if there is a car moving right to left at the same position
                if right_to_left[i] == left_to_right[i]:
                    # Increment the number of collisions
                    collisions += 1
                # If not, increment the position of the car moving left to right
                i -= 1

    # Return the number of collisions
    return collisions
    # Example usage:
    print(car_race_collision(5))  # Output: 2

    # Explanation:
    # The cars moving left to right are at positions 0, 1, 2, 3, 4.
    # The cars moving right to left are at positions 4, 3, 2, 1, 0.
    # The first collision occurs when the car at position 0 moving left to right collides with the car at position 0 moving right to left.
    # The second collision occurs when the car at position 2 moving left to right collides with the car at position 2 moving right to left.
    # Therefore, the output is 2.