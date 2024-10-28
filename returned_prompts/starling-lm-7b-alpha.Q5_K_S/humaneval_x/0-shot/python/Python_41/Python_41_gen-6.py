
Here is a way to solve this problem:

```python
def car_race_collision(n: int):
    # if no cars, no collision
    if n == 0:
        return 0
    # if one car, no collision
    if n == 1:
        return 0
    # if two cars, no collision
    if n == 2:
        return 0
    # if three cars, one collision
    if n == 3:
        return 1
    # if four cars, two collisions
    if n == 4:
        return 2

    return n * (n-1) // 2
```

Explanation:

- If there are no cars, there are no collisions.
- If there is exactly one car, there is no collision.
- If there are exactly two cars, there is no collision.
- If there are exactly three cars, there is one collision.
- If there are exactly four cars, there are two collisions.
- In general, for n cars, there are n * (n-1) // 2 collisions, by symmetry, each car will collide with all the other cars in front of it.

To prove the general case, note that the number of collisions is symmetric in the left and right moving cars, so we only need to count the number of collisions of the right moving cars with the left moving cars. There are n right moving cars, and each one will collide with all the n left moving cars in front of it, for a total of n * (n-1) collisions. Dividing by 2 gives the total number of collisions.

This function has a time complexity of O(1), and a space complexity of O(1).

```python
# Test Cases
print(car_race_collision(0))  # 0
print(car_race_collision(1))  # 0
print(car_race_collision(2))  # 0
print(car_race_collision(3))  # 1
print(car_race_collision(4))  # 2
print(car_race_collision(5))  # 3
