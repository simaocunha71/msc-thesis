```go
func Pluck(arr []int) []int {
    if len(arr) == 0 {
        return []int{}
    }

    smallestEven := math.MaxInt
    smallestIndex := -1

    for i, v := range arr {
        if v%2 == 0 && v < smallestEven {
            smallestEven = v
            smallestIndex = i
        }
    }

    if smallestIndex == -1 {
        return []int{}
    }

    return []int{smallestEven, smallestIndex}
}
```
