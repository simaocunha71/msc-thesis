Here is a solution in Go:

```go
import (
    "math"
)

func MaxFill(grid [][]int, capacity int) int {
    rows, cols := len(grid), len(grid[0])
    maxFill := 0
    for row := 0; row < rows; row++ {
        for col := 0; col < cols; col++ {
            if grid[row][col] == 1 {
                maxFill += capacity
            }
        }
    }
    return maxFill
}
```

This function iterates over each cell in the grid. If the cell has water (i.e., `grid[row][col] == 1`), it adds the bucket capacity to the maximum fill count. This is because each bucket can hold the specified capacity of water, and each unit of water requires a bucket to be lowered once. The function returns the total number of times the buckets need to be lowered.

For example, in the first example, the grid is `[[0,0,1,0], [0,1,0,0], [1,1,1,1]]`. The function will count the number of water units in each row and add the bucket capacity to the count. The result is `6`, which is the number of times the buckets need to be lowered.

This solution has a time complexity of O(m*n), where m is the number of rows and n is the number of columns in the grid. This is because it needs to iterate over each cell in the grid once. The space complexity is O(1), as it only uses a constant amount of space to store the maximum fill count and the grid dimensions.