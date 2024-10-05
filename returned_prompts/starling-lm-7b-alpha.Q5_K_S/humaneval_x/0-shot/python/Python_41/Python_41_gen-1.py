

def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right;  simultaneously, a different set of n cars
    are driving right to left.   The two sets of cars start out being very far from
    each other.  All cars move in the same speed.  Two cars are said to collide
    when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    This function outputs the number of such collisions.
    """

    # The total number of possible collisions can be calculated using the formula:
    # n + (n - 1) + (n - 2) + ... + 1 = (n * (n + 1)) / 2
    # However, since each car can only collide with one car from the opposite direction,
    # the maximum number of collisions is min(n, n). In other words, if there are 3 cars
    # moving in the same direction, at most 3 cars can collide with a car from the opposite
    # direction.

    # To determine the actual number of collisions, we can use the following logic:
    # - For each car in the left-to-right direction, there is a 50% chance it will collide with
    #   a car in the right-to-left direction. Since each car can only collide with one car from
    #   the opposite direction, the probability of the first car colliding is 1/2, the probability
    #   of the second car colliding is 1/2 * 1/2, the probability of the third car colliding is 1/2 * 1/2 * 1/2,
    #   and so on.
    # - The expected number of collisions can be calculated as the sum of this geometric series.

    # Using the formula for the sum of a geometric series, the expected number of collisions is given by:
    # n * (1 - (1/2)^n) /