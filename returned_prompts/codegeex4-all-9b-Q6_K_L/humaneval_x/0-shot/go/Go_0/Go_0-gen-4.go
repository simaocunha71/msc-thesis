```go
func HasCloseElements(numbers []float64, threshold float64) bool {
    if len(numbers) < 2 {
        return false
    }
    for i := 0; i < len(numbers); i++ {
        for j := i + 1; j < len(numbers); j++ {
            if math.Abs(numbers[i]-numbers[j]) < threshold {
                return true
            }
        }
    }
    return false
}
```
