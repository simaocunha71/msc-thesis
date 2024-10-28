```go
func DoubleTheDifference(lst []float64) int {
    sum := 0
    for _, val := range lst {
        if val > 0 && val == math.Floor(val) && val%2 == 1 {
            sum += int(val * val)
        }
    }
    return sum
}
```