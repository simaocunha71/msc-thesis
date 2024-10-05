Here is a simple Go function that accomplishes the task:

```go
import (
    "math"
)

// From a given list of integers, generate a list of rolling maximum element found until given moment
// in the sequence.
// >>> RollingMax([1, 2, 3, 2, 3, 4, 2])
// [1, 2, 3, 3, 3, 4, 4]
func RollingMax(numbers []int) []int {
    result := make([]int, len(numbers))
    result[0] = numbers[0]
    for i := 1; i < len(numbers); i++ {
        result[i] = math.Max(result[i-1], numbers[i])
    }
    return result
}
```

This function initializes a result slice with the same length as the input slice. It then iterates over the input slice, updating each element in the result slice to be the maximum of the current element and the previous element in the result slice. The function returns the result slice.