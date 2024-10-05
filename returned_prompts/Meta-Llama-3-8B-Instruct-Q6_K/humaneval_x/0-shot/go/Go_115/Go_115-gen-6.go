```go
func MaxFill(grid [][]int, capacity int) int {
    rows, cols := len(grid), len(grid[0])
    var result int
    for i := 0; i < rows; i++ {
        for j := 0; j < cols; j++ {
            if grid[i][j] == 1 {
                result += capacity
            }
        }
    }
    return result
}
```

The problem is asking to calculate the total number of times the buckets need to be lowered, given the grid of wells and the capacity of the buckets. The approach is to iterate over each cell in the grid and add the capacity to the result for each cell that has a value of 1.

For example, if the grid is [[0,0,1,0], [0,1,0,0], [1,1,1,1]] and the bucket capacity is 1, the result would be 6, because the buckets need to be lowered 6 times to extract all the water from the wells.

The time complexity of this solution is O(rows*cols), where rows and cols are the number of rows and columns in the grid. The space complexity is O(1), because we only use a constant amount of space to store the result.