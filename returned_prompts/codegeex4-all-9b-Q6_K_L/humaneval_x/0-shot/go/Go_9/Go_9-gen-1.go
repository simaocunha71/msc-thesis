Here is the Go code to solve the problem:

```go
func RollingMax(numbers []int) []int {
    maxSoFar := math.MinInt
    result := make([]int, 0, len(numbers))
    for _, num := range numbers {
        maxSoFar = max(num, maxSoFar)
        result = append(result, maxSoFar)
    }
    return result
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
```

The `RollingMax` function iterates over the input list of numbers. For each number, it calculates the maximum value found so far and appends it to the result list. The `max` function is a helper function to find the maximum of two integers.

Note: This solution assumes that the input list is not empty. If the input list can be empty, you should add a check for this case in the `RollingMax` function.