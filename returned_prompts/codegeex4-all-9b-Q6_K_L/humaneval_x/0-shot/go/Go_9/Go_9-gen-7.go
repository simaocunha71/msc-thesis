```go
func RollingMax(numbers []int) []int {
    max := numbers[0]
    result := []int{max}
    for i := 1; i < len(numbers); i++ {
        if numbers[i] > max {
            max = numbers[i]
        }
        result = append(result, max)
    }
    return result
}
```