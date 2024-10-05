
    def max_fill(grid, capacity):
        water_units = sum(sum(row) for row in grid)
        return math.ceil(water_units / capacity)

    return max_fill(grid, capacity)


print(max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1)) # 6
print(max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2)) # 5
print(max_fill([[0,0,0], [0,0,0]], 5)) # 0

Explanation:

In the first example, the total number of units of water is 6 (3 in the first row, 2 in the second row and 3 in the third row). So we need to lower the buckets 6 times to empty all the wells.

In the second example, the total number of units of water is 9 (5 in the first and second rows, and 4 in the third and fourth rows). So we need to lower the buckets 5 times to empty all the wells.

In the third example, there is no water in the grid, so we don't need to lower the buckets.

The time complexity of this solution is O(n*m) where n and m are the dimensions of the grid. This is because we are iterating through each cell of the grid once. The space complexity is O(1) as we are not using any additional space that scales with the size of the input.

The solution assumes that the bucket can hold an integer number of units of water. If the bucket can hold a fractional number of units, you would need to modify the solution to handle this case.
"""

# Solution Approach
"""
We first count the total number of water units in the grid. We then divide this total by the capacity of the bucket to get the number of times we need to lower the bucket. We round up this number because we can't partially fill the bucket.
"""

# Time Complexity
"""
O(n*m) where n and