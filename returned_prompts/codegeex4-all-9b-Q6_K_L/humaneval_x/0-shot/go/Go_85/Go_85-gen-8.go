```go
func Add(lst []int) int {
    sum := 0
    for i, v := range lst {
        if i%2 == 1 && v%2 == 0 {
            sum += v
        }
    }
    return sum
}
```