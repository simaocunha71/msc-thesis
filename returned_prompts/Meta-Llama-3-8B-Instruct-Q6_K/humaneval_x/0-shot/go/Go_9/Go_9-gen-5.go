Here is a simple function that calculates the rolling maximum of a list of integers:

```go
import (
    "math"
)

func RollingMax(numbers []int) []int {
    result := make([]int, len(numbers))
    result[0] = numbers[0]
    max := numbers[0]
    for i := 1; i < len(numbers); i++ {
        if numbers[i] > max {
            max = numbers[i]
        }
        result[i] = max
    }
    return result
}
```

This function initializes an empty slice `result` with the same length as the input slice `numbers`. It then iterates over the input slice, updating the maximum value `max` and the corresponding value in the `result` slice. The function finally returns the `result` slice. 

For example, if you call `RollingMax([1, 2, 3, 2, 3, 4, 2])`, it will return `[1, 2, 3, 3, 3, 4, 4]`. 

This function assumes that the input slice is not empty. If the input slice can be empty, you should add a check at the beginning of the function. 

Also, note that this function has a time complexity of O(n), where n is the length of the input slice, because it needs to iterate over the input slice once. The space complexity is also O(n) because it needs to store the result slice. 