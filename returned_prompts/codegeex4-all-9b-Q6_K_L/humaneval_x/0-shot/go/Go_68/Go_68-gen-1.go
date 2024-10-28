```go
func Pluck(arr []int) []int {
    if len(arr) == 0 {
        return []int{}
    }
    smallestEven := math.MaxInt
    index := -1
    for i, num := range arr {
        if num%2 == 0 && num < smallestEven {
            smallestEven = num
            index = i
        }
    }
    if index == -1 {
        return []int{}
    }
    return []int{smallestEven, index}
}
```
