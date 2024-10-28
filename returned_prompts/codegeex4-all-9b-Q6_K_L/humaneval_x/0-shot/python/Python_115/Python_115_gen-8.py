def max_fill(grid, capacity):
    import math
    total = 0
    for row in grid:
        for i in row:
            total += math.ceil(i / capacity)
    return total

print(max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1)) # 6
print(max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2)) # 5
print(max_fill([[0,0,0], [0,0,0]], 5)) # 0