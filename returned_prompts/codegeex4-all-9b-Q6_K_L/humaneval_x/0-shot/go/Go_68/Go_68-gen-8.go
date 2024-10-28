```go
func Pluck(arr []int) []int {
    if len(arr) == 0 {
        return []int{}
    }
    var smallestEven int = math.MaxInt32
    var smallestEvenIndex int = -1
    for i, val := range arr {
        if val%2 == 0 && val < smallestEven {
            smallestEven = val
            smallestEvenIndex = i
        }
    }
    if smallestEvenIndex == -1 {
        return []int{}
    }
    return []int{smallestEven, smallestEvenIndex}
}
```