```go
func MakeAPile(n int) []int {
    arr := []int{n}
    for i := 1; i < n; i++ {
        if n % 2 == 0 {
            arr = append(arr, n + 2)
        } else {
            arr = append(arr, n + 1)
        }
        n = n + 1
    }
    return arr
}
```
