Here is the solution:
```go
import (
    "math"
)

func RollingMax(numbers []int) []int {
    result := make([]int, len(numbers))
    maxSoFar := math.MinInt32

    for i, num := range numbers {
        if num > maxSoFar {
            maxSoFar = num
        }
        result[i] = maxSoFar
    }
    return result
}
```
Explanation:

* We create a new slice `result` to store the rolling maximum values.
* We initialize `maxSoFar` to the minimum possible integer value (`math.MinInt32`) to keep track of the maximum value seen so far.
* We iterate over the input slice `numbers` using a range loop.
* For each number, we check if it is greater than the current `maxSoFar`. If it is, we update `maxSoFar` to the new value.
* We assign the current `maxSoFar` value to the corresponding index in the `result` slice.
* Finally, we return the `result` slice.

Example usage