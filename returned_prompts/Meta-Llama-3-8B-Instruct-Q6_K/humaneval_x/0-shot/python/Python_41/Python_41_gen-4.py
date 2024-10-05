    # Initialize collision count to 0
    collisions = 0

    # Generate all pairs of cars that can collide
    for i in range(n):
        for j in range(n):
            # Check if the cars are moving in opposite directions
            if (i < j) and (i + j) % 2 == 1:
                # Increment collision count
                collisions += 1

    # Return the total number of collisions
    return collisions

n = int(input("Enter the number of cars: "))
print(car_race_collision(n))  # Output: The number of collisions for n cars.  # noqa: F841
# Test case: car_race_collision(4)  # Output: 3
# Test case: car_race_collision(6)  # Output: 5
# Test case: car_race_collision(8)  # Output: 7
# Test case: car_race_collision(10)  # Output: 9
# Test case: car_race_collision(12)  # Output: 11
# Test case: car_race_collision(14)  # Output: 13
# Test case: car_race_collision(16)  # Output: 15
# Test case: car_race_collision(18)  # Output: 17
# Test case: car_race_collision(20)  # Output: 19
# Test case: car_race_collision(22)  # Output: 21
# Test case: car_race_collision(24)  # Output: 23
# Test case: car_race_collision(26)  # Output: 25
# Test case: car_race_collision(28)  # Output: 27
# Test case: car_race_collision(30)  # Output: 29
# Test case: car_race_collision(32)  # Output: 31
# Test case: car_race_collision(34)  # Output: 33
# Test case: car_race_collision(36)  # Output: 35
# Test case: car_race_collision(38)  # Output: 37
# Test case: car_race_collision(40)  # Output: 39
# Test case: car_race_collision(42)  # Output: 41
# Test case: car_race_collision(44)  # Output: 43
# Test case: car_race_collision(46)  # Output: 45
# Test case: