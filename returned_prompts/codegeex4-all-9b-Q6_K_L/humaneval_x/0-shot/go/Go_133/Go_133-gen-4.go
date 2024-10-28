```go
func SumSquares(lst []float64) int {
    sum := 0
    for _, x := range lst {
        sum += int(math.Ceil(x)) * int(math.Ceil(x))
    }
    return sum
}
```