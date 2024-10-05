```go
func RollingMax(numbers []int) []int {
    maxSoFar := math.MinInt64
    result := make([]int, 0, len(numbers))
    for _, number := range numbers {
        if number > maxSoFar {
            maxSoFar = number
        }
        result = append(result, maxSoFar)
    }
    return result
}
```