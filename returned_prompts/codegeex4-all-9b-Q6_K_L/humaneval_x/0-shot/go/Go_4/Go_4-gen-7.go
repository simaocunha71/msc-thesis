```go
func MeanAbsoluteDeviation(numbers []float64) float64 {
    var sum float64
    for _, number := range numbers {
        sum += number
    }
    mean := sum / float64(len(numbers))

    var mad float64
    for _, number := range numbers {
        mad += math.Abs(number - mean)
    }
    mad /= float64(len(numbers))
    return mad
}
```
