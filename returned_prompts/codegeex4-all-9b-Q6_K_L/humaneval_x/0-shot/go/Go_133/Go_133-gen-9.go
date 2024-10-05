```go
func SumSquares(lst []float64) int {
    sum := 0
    for _, num := range lst {
        sum += int(math.Pow(math.Ceil(num), 2))
    }
    return sum
}
```
