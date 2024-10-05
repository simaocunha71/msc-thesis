```go
func SumSquares(lst []int) int {
    sum := 0
    for i, n := range lst {
        if i%3 == 0 {
            sum += n * n
        } else if i%4 == 0 {
            sum += n * n * n
        } else {
            sum += n
        }
    }
    return sum
}
```
