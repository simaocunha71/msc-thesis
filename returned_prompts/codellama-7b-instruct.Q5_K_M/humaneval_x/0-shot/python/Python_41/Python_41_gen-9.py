
    def car_race_collision(n):
        # Initialize the number of collisions to 0.
        collisions = 0

        # Initialize the distance between the leftmost and rightmost cars to 0.
        distance = 0

        # While the distance between the leftmost and rightmost cars is greater than 0
        while distance > 0:

            # Move the leftmost car one unit to the right.
            distance += 1

            # If the leftmost car hits the rightmost car
            if distance == n:
                # Increment the number of collisions.
                collisions += 1

            # Move the rightmost car one unit to the left.
            distance -= 1

            # If the rightmost car hits the leftmost car
            if distance == -n:
                # Increment the number of collisions.
                collisions += 1

        # Return the number of collisions.
        return collisions



