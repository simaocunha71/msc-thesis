```go
func RollingMax(numbers []int) []int {
    max := math.MinInt64
    result := make([]int, 0, len(numbers))
    for _, num := range numbers {
        if num > max {
            max = num
        }
        result = append(result, max)
    }
    return result
}
```