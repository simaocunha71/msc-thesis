Here is a simple Go solution for the problem:

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

This function iterates over the input slice `numbers`. For each number, it checks if it is greater than the current maximum found so far (`maxSoFar`). If it is, it updates `maxSoFar`. The maximum found so far is then stored in the `result` slice at the current position.

The time complexity of this solution is O(n), where n is the length of the input slice. The space complexity is also O(n), as we need to store the result in a new slice.