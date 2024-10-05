    def is_colliding(a: int, b: int) -> bool:
        return (a > 0 and b < 0) or (a < 0 and b > 0)

    collisions = 0
    for i in range(1, n):
        for j in range(i, n):
            if is_colliding(i, j):
                collisions += 1
    return collisions


