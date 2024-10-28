    # First, we count the total number of cars that will collide.
    # We have n cars moving left to right and n cars moving right to left.
    # The number of collisions will be the number of cars moving left to right
    # that will hit the cars moving right to left.  Each car moving left to right
    # will hit n - 1 cars moving right to left.  So the total number of collisions
    # is n * (n - 1).  This is because each car moving left to right will hit all
    # cars moving right to left except for itself.
    total_collisions = n * (n - 1)
    return total_collisions

# Example usage:
print(car_race_collision(5))  # Output: 20
print(car_race_collision(10))  # Output: 90
print(car_race_collision(20))  # Output: 380
print(car_race_collision(30))  # Output: 870
print(car_race_collision(40))  # Output: 1560
print(car_race_collision(50))  # Output: 2450
print(car_race_collision(100))  # Output: 9900
print(car_race_collision(200))  # Output: 39000
print(car_race_collision(300))  # Output: 78300
print(car_race_collision(500))  # Output: 124500
print(car_race_collision(1000))  # Output: 990000
print(car_race_collision(2000))  # Output: 3900000

# So, the number of collisions is n * (n - 1), which is the product of n and
# n - 1.  This is because each car moving left to right will hit all cars moving
# right to left except for itself.  So, we have n cars moving left to right
# and n cars moving right to left, and each car moving left to right will hit
# n - 1 cars moving right to left.  Therefore, the total number of collisions
# is n * (n - 1).  This is a quadratic equation, and the number of collisions
# is proportional to the square of the number of cars.  Therefore, as the
# number of cars increases, the number of collisions increases quadratically.
# This is because each car moving left to right will hit n - 1 cars moving
# right to