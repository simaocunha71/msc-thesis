```
def car_race_collision(n: int):
    collisions = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (i + j) % 2 == 0:
                collisions += 1
    return collisions
```
This function counts the number of collisions between the cars. Each car is represented by its position on the road, with cars moving to the right having a positive position and cars moving to the left having a negative position. The function iterates over each pair of cars and checks if they will collide by seeing if the sum of their positions is even. If it is, the cars will collide, so the function increments the collision count. Finally, the function returns the total number of collisions.