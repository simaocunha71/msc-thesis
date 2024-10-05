```go
func DoubleTheDifference(lst []float64) int {
    sum := 0
    for _, v := range lst {
        if v > 0 && v == math.Floor(v) && v%2 == 1 {
            sum += int(math.Pow(v, 2))
        }
    }
    return sum
}
```