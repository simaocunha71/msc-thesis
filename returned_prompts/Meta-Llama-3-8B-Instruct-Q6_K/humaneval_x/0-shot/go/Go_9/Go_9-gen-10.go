Here is a simple Go function that generates the rolling maximum element found until a given moment in the sequence.

```go
import (
    "math"
)

func RollingMax(numbers []int) []int {
    result := make([]int, len(numbers))
    max := math.MinInt32
    for i, num := range numbers {
        if num > max {
            max = num
        }
        result[i] = max
    }
    return result
}
```

This function iterates over the input slice, keeping track of the maximum value seen so far. It stores this maximum value in the result slice at each position. The function returns the result slice.

You can use it like this:

```go
numbers := []int{1, 2, 3, 2, 3, 4, 2}
result := RollingMax(numbers)
fmt.Println(result) // Output: [1 2 3 3 3 4 4]
``` 





