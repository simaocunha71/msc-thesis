```go
func RollingMax(numbers []int) []int {
    if len(numbers) == 0 {
        return []int{}
    }
    max := numbers[0]
    result := []int{max}
    for _, n := range numbers[1:] {
        if n > max {
            max = n
        }
        result = append(result, max)
    }
    return result
}
```