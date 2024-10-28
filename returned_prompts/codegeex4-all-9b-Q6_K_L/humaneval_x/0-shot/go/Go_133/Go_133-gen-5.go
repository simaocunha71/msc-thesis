```go
func SumSquares(lst []float64) int {
    var sum float64 = 0
    for _, num := range lst {
        sum += math.Pow(math.Ceil(num), 2)
    }
    return int(sum)
}
```