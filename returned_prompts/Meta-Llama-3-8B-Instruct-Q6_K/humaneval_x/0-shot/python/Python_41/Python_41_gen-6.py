def car_race_collision(n: int):
    collisions = 0

    # Initialize the positions of the cars
    left_cars = [i for i in range(n)]
    right_cars = [i for i in range(2 * n - 1, 2 * n - 1 - n, -1)]

    while True:
        # Check for collisions
        for i in range(len(left_cars)):
            for j in range(len(right_cars)):
                if left_cars[i] == right_cars[j]:
                    collisions += 1
                    left_cars[i] += 1
                    right_cars[j] -= 1
        # Move all the cars
        left_cars = [pos + 1 for pos in left_cars]
        right_cars = [pos - 1 for pos in right_cars]
        # Check if all cars are moving away from each other
        if not (set(left_cars) & set(right_cars)):
            break

    return collisions
# test the function
print(car_race_collision(2))  # Expected output: 2
print(car_race_collision(3))  # Expected output: 6
print(car_race_collision(4))  # Expected output: 12
print(car_race_collision(5))  # Expected output: 20
print(car_race_collision(6))  # Expected output: 30
print(car_race_collision(7))  # Expected output: 42
print(car_race_collision(8))  # Expected output: 56
print(car_race_collision(9))  # Expected output: 72
print(car_race_collision(10))  # Expected output: 90
print(car_race_collision(11))  # Expected output: 110
print(car_race_collision(12))  # Expected output: 132
print(car_race_collision(13))  # Expected output: 156
print(car_race_collision(14))  # Expected output: 182
print(car_race_collision(15))  # Expected output: 210
print(car_race_collision(16))  # Expected output: 240
print(car_race_collision(17))  # Expected output: 272
print(car_race_collision(18))  # Expected output: 306
print(car_race_collision(19))  # Expected output: 342
print(car_race_collision(20))  # Expected output: 380
print(car_race_collision(21))  #