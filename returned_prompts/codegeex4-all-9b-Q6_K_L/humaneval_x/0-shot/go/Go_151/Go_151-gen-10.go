```go
func DoubleTheDifference(lst []float64) int {
    total := 0
    for _, n := range lst {
        if n >= 0 && math.Mod(n, 1) == 0 && n%2 != 0 {
            total += int(math.Pow(n, 2))
        }
    }
    return total
}
```