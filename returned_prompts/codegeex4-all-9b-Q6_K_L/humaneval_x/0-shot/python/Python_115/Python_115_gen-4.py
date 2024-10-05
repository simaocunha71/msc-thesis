def max_fill(grid, capacity):
    import math
    max_count = 0
    for i in range(len(grid)):
        well = grid[i]
        for j in range(len(well)):
            if well[j] == 1:
                count = math.ceil(well[j]/capacity)
                max_count += count
    return max_count

grid1 = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
grid2 = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
grid3 = [[0,0,0], [0,0,0]]
capacity1 = 1
capacity2 = 2
capacity3 = 5
print(max_fill(grid1, capacity1)) # 6
print(max_fill(grid2, capacity2)) # 5
print(max_fill(grid3, capacity3)) # 0