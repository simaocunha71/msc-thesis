

def car_race_collision(n: int):
    if n == 0:
        return 0
    return n * (n - 1) // 2


# Car race collision
# Imagine a road that's a perfectly straight infinitely long line.
# n cars are driving left to right;  simultaneously, a different set of n cars
# are driving right to left.   The two sets of cars start out being very far from
# each other.  All cars move in the same speed.  Two cars are said to collide
# when a car that's moving left to right hits a car that's moving right to left.
# However, the cars are infinitely sturdy and strong; as a result, they continue moving
# in their trajectory as if they did not collide.

# This function outputs the number of such collisions.
# car_race_collision(n: int) -> int:

# Examples:
# car_race_collision(1) == 0
# car_race_collision(2) == 0
# car_race_collision(3) == 1
# car_race_collision(4) == 3
# car_race_collision(5) == 6
# car_race_collision(100) == 33450

# Solution
def car_race_collision(n: int):
    if n == 0:
        return 0
    return n * (n - 1) // 2

# Tests
assert(car_race_collision(1) == 0)
assert(car_race_collision(2) == 0)
assert(car_race_collision(3) == 1)
assert(car_race_collision(4) == 3)
assert(car_race_collision(5) == 6)
assert(car_race_collision(100) == 33450)

print("All tests passed.")






```

```
def car_race_collision(n: int):
    if n