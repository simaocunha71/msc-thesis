Here is the solution in Go:
```go
package main

import (
    "math"
    "fmt"
)

// From a given list of integers, generate a list of rolling maximum element found until given moment
// in the sequence.
// >>> RollingMax([1, 2, 3, 2, 3, 4, 2])
// [1, 2, 3, 3, 3, 4, 4]
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

func main() {
    numbers := []int{1, 2, 3, 2, 3, 4, 2}
    fmt.Println(RollingMax(numbers))
}
```
This solution uses a slice to store the rolling maximum values, and a variable `maxSoFar` to keep track of the maximum value seen so far. It iterates over the input slice, updating `maxSoFar` and the `result` slice as it goes. The `result` slice is then returned. The `main` function demonstrates the usage of the `RollingMax` function. 

The output of the program will be: `[1 2 3 3 3 4 4]`, which is the rolling maximum of the input slice. 

The time complexity of this solution is O(n), where n is the length of the input slice, because it makes a single pass over the input slice. The space complexity is also O(n), because it creates a new slice of the same length as the input slice. 