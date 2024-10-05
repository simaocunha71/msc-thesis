Here is the solution:

```go
func MaxFill(grid [][]int, capacity int) int {
    rows, cols := len(grid), len(grid[0])
    res := 0
    for row := 0; row < rows; row++ {
        for col := 0; col < cols; col++ {
            if grid[row][col] == 1 {
                res += capacity
            }
        }
    }
    return res
}
```

Explanation:
The problem is asking to find the total number of times the buckets need to be lowered, which is equivalent to the total number of units of water in all wells. The buckets can hold a certain capacity of water, but in this case, since all buckets have the same capacity, we can simply count the number of 1's in the grid, which represents the units of water in each well. 

The solution iterates over each cell in the grid and increments the result by the bucket capacity for each cell that contains a 1. This way, we count the total number of units of water in all wells, which is the total number of times the buckets need to be lowered. 

Time complexity: O(rows * cols), where rows and cols are the number of rows and columns in the grid. 
Space complexity: O(1), as we are using a constant amount of space to store the result and the grid dimensions. 