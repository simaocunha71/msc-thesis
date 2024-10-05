```go
func RollingMax(numbers []int) []int {
    if len(numbers) == 0 {
        return []int{}
    }

    max := numbers[0]
    result := []int{max}

    for _, num := range numbers[1:] {
        if num > max {
            max = num
        }
        result = append(result, max)
    }

    return result
}
```
