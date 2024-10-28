```go
func MeanAbsoluteDeviation(numbers []float64) float64 {
    if len(numbers) == 0 {
        return 0.0
    }

    mean := 0.0
    for _, num := range numbers {
        mean += num
    }
    mean /= float64(len(numbers))

    mad := 0.0
    for _, num := range numbers {
        mad += math.Abs(num - mean)
    }
    mad /= float64(len(numbers))

    return mad
}
```