```go
func RollingMax(numbers []int) []int {
    var max, result []int
    for _, n := range numbers {
        if len(max) == 0 || n > max[len(max)-1] {
            max = append(max, n)
        }
        result = append(result, max[len(max)-1])
    }
    return result
}
```
