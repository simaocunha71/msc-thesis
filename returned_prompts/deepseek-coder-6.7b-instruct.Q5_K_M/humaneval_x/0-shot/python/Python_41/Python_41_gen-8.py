
    # initialize the count of collisions
    collisions = 0

    # for each car moving left to right
    for i in range(n):
        # for each car moving right to left
        for j in range(n):
            # if the cars collide
            if i == j:
                # increment the collision count
                collisions += 1

    # return the total number of collisions
    return collisions

# test the function with some example inputs
print(car_race_collision(2))  # expected output: 2
print(car_race_collision(3))  # expected output: 3
print(car_race_collision(4))  # expected output: 4

