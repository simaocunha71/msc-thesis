Here is the implementation in Go:
```go
import (
    "math"
)

func RollingMax(numbers []int) []int {
    result := make([]int, len(numbers))
    result[0] = numbers[0]
    maxSoFar := numbers[0]
    for i := 1; i < len(numbers); i++ {
        if numbers[i] > maxSoFar {
            maxSoFar = numbers[i]
        }
        result[i] = maxSoFar
    }
    return result
}
```
This function initializes the result array with the same length as the input array. It then iterates over the input array, keeping track of the maximum number seen so far. For each number, it updates the maximum seen so far if the current number is larger, and then stores this maximum in the result array. The function finally returns the result array.

For example, if you call `RollingMax([1, 2, 3, 2, 3, 4, 2])`, the function will return `[1, 2, 3, 3, 3, 4, 4]`.