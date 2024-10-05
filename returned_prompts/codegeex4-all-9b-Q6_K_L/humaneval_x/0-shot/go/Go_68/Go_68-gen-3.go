```go
func Pluck(arr []int) []int {
    if len(arr) == 0 {
        return []int{}
    }
    
    min := math.MaxInt
    minIndex := -1
    
    for i, v := range arr {
        if v%2 == 0 && v < min {
            min = v
            minIndex = i
        }
    }
    
    if minIndex == -1 {
        return []int{}
    }
    
    return []int{arr[minIndex], minIndex}
}
```
