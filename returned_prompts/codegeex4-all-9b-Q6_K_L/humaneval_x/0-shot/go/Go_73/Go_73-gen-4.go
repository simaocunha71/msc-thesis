```go
func SmallestChange(arr []int) int {
    if len(arr) == 0 {
        return 0
    }
    if len(arr) == 1 {
        return 0
    }
    count := 0
    for i := 0; i < len(arr)/2; i++ {
        if arr[i] != arr[len(arr)-i-1] {
            count++
        }
    }
    return count
}
```
