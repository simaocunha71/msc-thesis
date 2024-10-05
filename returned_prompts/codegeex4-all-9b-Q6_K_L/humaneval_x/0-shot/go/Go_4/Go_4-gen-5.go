```go
func MeanAbsoluteDeviation(numbers []float64) float64 {
    // Calculate mean of the numbers
    mean := 0.0
    for _, num := range numbers {
        mean += num
    }
    mean /= float64(len(numbers))

    // Calculate mean absolute deviation
    mad := 0.0
    for _, num := range numbers {
        mad += math.Abs(num - mean)
    }
    mad /= float64(len(numbers))

    return mad
}
```
