Here is a Go solution for the problem:

```go
import (
    "math"
)

func MaxFill(grid [][]int, capacity int) int {
    maxFill := 0
    for i := 0; i < len(grid); i++ {
        for j := 0; j < len(grid[i]); j++ {
            if grid[i][j] == 1 {
                maxFill += capacity
            }
        }
    }
    return maxFill
}
```

This function goes through each cell in the grid and adds the capacity to the total fill if the cell contains water (i.e., grid[i][j] == 1). This will give us the total fill required to empty all the wells. 

This solution assumes that the capacity of the bucket is given and that we need to find the total fill required to empty all the wells. 

For example, if the grid is `[[0,0,1,0], [0,1,0,0], [1,1,1,1]]` and the capacity is 1, the function will return 6, which is the total fill required to empty all the wells. 

The time complexity of this solution is O(m*n), where m is the number of rows and n is the number of columns in the grid. The space complexity is O(1), as we are using a constant amount of space to store the maximum fill. 





Please note that this is a simple solution and it does not take into account the actual process of filling the buckets and lowering them. It just calculates the total fill required to empty all the wells. If you need to implement the actual process, you would need a more complex solution.