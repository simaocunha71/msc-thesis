def makeAPile(n):
    levels = []
    stones = n
    while stones > 0:
        levels.append(stones)
        stones += 2 if n % 2 != 0 else 1
        n -= 1
    return levels

print(makeAPile(3))