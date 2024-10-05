```go
func SumSquares(lst []float64) int {
    var sum int
    for _, num := range lst {
        sum += int(math.Pow(math.Ceil(num), 2))
    }
    return sum
}
```
