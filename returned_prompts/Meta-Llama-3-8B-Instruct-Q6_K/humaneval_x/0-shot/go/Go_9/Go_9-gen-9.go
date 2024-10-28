Here is a simple implementation of the function in Go:

```go
import (
    "math"
)

func RollingMax(numbers []int) []int {
    var result []int
    max := math.MinInt32
    for _, num := range numbers {
        if num > max {
            max = num
        }
        result = append(result, max)
    }
    return result
}
```

This function iterates over the input slice of integers, keeping track of the maximum value seen so far. It appends this maximum value to the result slice at each iteration. At the end, the function returns the result slice. The `math.MinInt32` is used as the initial maximum value to handle the case when the input slice is empty.

You can call this function with a slice of integers like this:

```go
numbers := []int{1, 2, 3, 2, 3, 4, 2}
result := RollingMax(numbers)
fmt.Println(result) // Output: [1 2 3 3 3 4 4]
```  