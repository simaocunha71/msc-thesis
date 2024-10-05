```go
func DoubleTheDifference(lst []float64) int {
    sum := 0
    for _, x := range lst {
        if x >= 0 && x == math.Floor(x) && x%2 == 1 {
            sum += int(math.Pow(x, 2))
        }
    }
    return sum
}
```