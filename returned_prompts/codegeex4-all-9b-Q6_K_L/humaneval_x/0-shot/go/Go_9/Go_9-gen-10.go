```go
func RollingMax(numbers []int) []int {
    rollingMaxes := make([]int, len(numbers))
    currentMax := math.MinInt64

    for i, num := range numbers {
        if num > currentMax {
            currentMax = num
        }
        rollingMaxes[i] = currentMax
    }

    return rollingMaxes
}
```