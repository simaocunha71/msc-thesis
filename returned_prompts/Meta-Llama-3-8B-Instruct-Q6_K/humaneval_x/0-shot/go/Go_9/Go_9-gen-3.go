Here is a simple implementation in Go:

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

This function initializes an empty result slice and a variable `max` to keep track of the maximum number seen so far. It then iterates over the input slice, updating the `max` variable whenever it encounters a number greater than the current maximum. It also updates the corresponding element in the result slice with the current maximum. Finally, it returns the result slice. 

This function has a time complexity of O(n), where n is the length of the input slice, as it makes a single pass over the input slice. It has a space complexity of O(n) as well, as it needs to store the result slice. 

You can test this function with the example you provided:

```go
numbers := []int{1, 2, 3, 2, 3, 4, 2}
result := RollingMax(numbers)
fmt.Println(result) // Output: [1 2 3 3 3 4 4]
``` 