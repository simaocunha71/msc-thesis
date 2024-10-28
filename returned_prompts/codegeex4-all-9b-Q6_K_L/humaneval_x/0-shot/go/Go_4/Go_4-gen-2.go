```go
func MeanAbsoluteDeviation(numbers []float64) float64 {
    mean := 0.0
    for _, num := range numbers {
        mean += num
    }
    mean /= float64(len(numbers))

    sum := 0.0
    for _, num := range numbers {
        sum += math.Abs(num - mean)
    }
    return sum / float64(len(numbers))
}
```