Here is a solution in Go:

```go
import (
    "math"
)

func MaxFill(grid [][]int, capacity int) int {
    var total int
    for _, row := range grid {
        for _, cell := range row {
            if cell == 1 {
                total += 1
            }
        }
    }
    return total / capacity + (total % capacity > 0)
}
```

The idea is to calculate the total amount of water in the grid and then divide it by the bucket capacity. The remainder of the division is the number of extra units of water that cannot be filled by the buckets. If the remainder is greater than 0, we add 1 to the result to account for the extra bucket needed to fill the remaining water.

For example, if the total amount of water is 12 and the bucket capacity is 3, we need 4 buckets to fill the water (12 / 3 = 4, remainder 0). If the remainder is 1 (e.g., 11 / 3 = 3, remainder 2), we need 4 buckets and an extra bucket to fill the remaining water, so the result is 5. If the remainder is 0, we only need the calculated number of buckets.