```go
func Pluck(arr []int) []int {
    result := []int{}
    if len(arr) == 0 {
        return result
    }
    even := math.MaxInt
    index := -1
    for i, num := range arr {
        if num%2 == 0 && num < even {
            even = num
            index = i
        }
    }
    if index != -1 {
        result = append(result, even, index)
    }
    return result
}
```
