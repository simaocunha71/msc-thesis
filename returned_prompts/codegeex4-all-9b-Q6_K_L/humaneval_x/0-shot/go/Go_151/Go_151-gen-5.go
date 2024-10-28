```go
func DoubleTheDifference(lst []float64) int {
    result := 0
    for _, i := range lst {
        if i > 0 && i == math.Floor(i) && i%2 != 0 {
            result += int(i*i)
        }
    }
    return result
}
```