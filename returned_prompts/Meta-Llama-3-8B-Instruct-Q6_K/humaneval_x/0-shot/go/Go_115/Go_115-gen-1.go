The problem can be solved by iterating over the grid and for each cell, checking if it is a well (i.e., its value is 1) and if its bucket is not full yet. If it is a well and its bucket is not full, we lower the bucket by the capacity and increment the count of times we need to lower the buckets. We also update the state of the well by setting its value to 0.

Here is the solution:
```go
func MaxFill(grid [][]int, capacity int) int {
    var count int
    for i := 0; i < len(grid); i++ {
        for j := 0; j < len(grid[i]); j++ {
            if grid[i][j] == 1 {
                if capacity > 0 {
                    grid[i][j] = 0
                    count++
                    capacity--
                }
            }
        }
    }
    return count
}
```
This solution has a time complexity of O(m*n), where m is the number of rows in the grid and n is the number of columns. This is because we are iterating over each cell in the grid once.

The space complexity is O(1), as we are using a constant amount of space to store the count and the capacity. We are not using any extra space that scales with the input size.