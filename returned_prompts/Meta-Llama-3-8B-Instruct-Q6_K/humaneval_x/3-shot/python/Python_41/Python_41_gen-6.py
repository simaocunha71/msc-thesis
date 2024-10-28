    collisions = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                if (i + j) % 2 == 0:
                    collisions += 1

    return collisions // 2


