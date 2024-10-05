```go
func MeanAbsoluteDeviation(numbers []float64) float64 {
    avg := average(numbers)
    mad := 0.0
    for _, number := range numbers {
        mad += math.Abs(number - avg)
    }
    return mad / float64(len(numbers))
}

func average(numbers []float64) float64 {
    sum := 0.0
    for _, number := range numbers {
        sum += number
    }
    return sum / float64(len(numbers))
}
```