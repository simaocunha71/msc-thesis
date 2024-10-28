```go
func Pluck(arr []int) []int {
    if len(arr) == 0 {
        return []int{}
    }

    min := math.MaxInt
    minIndex := -1

    for i, value := range arr {
        if value%2 == 0 && value < min {
            min = value
            minIndex = i
        }
    }

    if minIndex == -1 {
        return []int{}
    }

    return []int{min, minIndex}
}
```

