```go
func HasCloseElements(numbers []float64, threshold float64) bool {
    for _, n := range numbers {
        for _, m := range numbers {
            if math.Abs(n-m) < threshold && n != m {
                return true
            }
        }
    }
    return false
}
```