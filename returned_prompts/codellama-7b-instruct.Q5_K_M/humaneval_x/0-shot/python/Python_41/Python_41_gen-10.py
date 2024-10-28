
    """
    Here's the basic idea of the algorithm:

    We'll maintain two arrays:
    - One for the left-to-right cars
    - One for the right-to-left cars

    We'll initialize both arrays with a single element each, at the starting position
    of the leftmost car and the rightmost car.
    We'll then iterate through the cars and add new cars to the arrays as we go.
    At each iteration, we'll check to see if the two arrays overlap.  If they do,
    we'll add another collision to the total.
    """
    def car_race_collision(n):
        left_to_right = [0]
        right_to_left = [n-1]
        total_collisions = 0

        for i in range(1, n):
            left_to_right.append(left_to_right[-1] + 1)
            right_to_left.append(right_to_left[-1] - 1)

            if left_to_right[-1] in right_to_left:
                total_collisions += 1

        return total_collisions

