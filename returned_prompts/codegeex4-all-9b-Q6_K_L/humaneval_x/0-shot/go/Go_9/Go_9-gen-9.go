```go
func RollingMax(numbers []int) []int {
    max := math.MinInt32
    result := make([]int, 0, len(numbers))
    for _, n := range numbers {
        max = int(math.Max(float64(max), float64(n)))
        result = append(result, max)
    }
    return result
}
```