```go
func Pluck(arr []int) []int {
    if len(arr) == 0 {
        return []int{}
    }
    min := arr[0]
    minIndex := 0
    for i, v := range arr {
        if v%2 == 0 && v < min {
            min = v
            minIndex = i
        }
    }
    if min == arr[0] && arr[0]%2 == 0 {
        return []int{arr[0], 0}
    }
    if min == arr[len(arr)-1] && arr[len(arr)-1]%2 == 0 {
        return []int{arr[len(arr)-1], len(arr)-1}
    }
    return []int{min, minIndex}
}
```
