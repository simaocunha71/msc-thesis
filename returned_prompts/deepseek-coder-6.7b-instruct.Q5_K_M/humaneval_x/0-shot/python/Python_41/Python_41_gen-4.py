
    # the total number of collisions is equal to the sum of the positions of all the cars
    # since each car moves to the left or right by one unit, the position of the car is 
    # the index of the car in the list plus one

    # if a car is moving left, its position is negative
    # if a car is moving right, its position is positive
    # the total number of collisions is the sum of the positions of all the cars

    total_collisions = 0
    for i in range(n):
        left_car_position = -(i + 1)
        right_car_position = n - i
        total_collisions += abs(left_car_position - right_car_position)

    return total_collisions


print(car_race_collision(3))
print(car_race_collision(4))
print(car_race_collision(5))

# Expected output:
# 2
# 4
# 6
<jupyter_output>
2
4
6
<jupyter_text>
Problem 3: 2D list (lists within lists) manipulation**