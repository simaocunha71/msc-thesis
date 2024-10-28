```go
func MeanAbsoluteDeviation(numbers []float64) float64 {
    var sum float64 = 0.0
    for _, num := range numbers {
        sum += num
    }
    mean := sum / float64(len(numbers))
    var mad float64 = 0.0
    for _, num := range numbers {
        mad += math.Abs(num - mean)
    }
    return mad / float64(len(numbers))
}
```