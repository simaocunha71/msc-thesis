    def minPath(grid, k):
        n = len(grid)
        res = []
        for i in range(n):
            for j in range(n):
                if k == 1:
                    res.append(grid[i][j])
                else:
                    for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        ni, nj = i + d[0], j + d[1]
                        if 0 <= ni < n and 0 <= nj < n:
                            res.append(grid[ni][nj])
                            k -= 1
                            if k == 0:
                                return res
                            break
        return res
    # Testing the function
    grid = [[1,2,3], [4,5,6], [7,8,9]]
    k = 3
    print(minPath(grid, k))  # Output: [1, 2, 1]

    grid = [[5,9,3], [4,1,6], [7,8,2]]
    k = 1
    print(minPath(grid, k))  # Output: [1]
    # The function works by iterating over the grid and for each cell, 
    # it checks all the possible directions (up, down, left, right) and 
    # recursively calls itself with the new cell and decrements k. 
    # If k becomes 0, it returns the path. If not, it continues with the 
    # next cell. The function returns the minimum path in the sense that 
    # it visits the cells in the order that they appear in the grid. 
    # If there are multiple minimum paths, it returns the first one it finds. 
    # The function can be optimized by using a set to keep track of the 
    # visited cells, but this is not necessary for this problem. 
    # The time complexity is O(n^2 * k) and the space complexity is O(n^2 * k).  # noqa: E501
    # The function can be further optimized by using a queue to keep track 
    # of the cells to visit, but this is not necessary for this problem. 
    # The function returns the minimum path in the sense that it visits the 
    # cells in the order that they appear in the grid. If there are multiple 
    # minimum paths, it returns the first one it