```go
func SumSquares(lst []int) int {
    sum := 0
    for i, x := range lst {
        if i%3 == 0 {
            sum += x * x
        }
        if i%4 == 0 && i%3 != 0 {
            sum += x * x * x
        }
    }
    return sum
}
```