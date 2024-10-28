```go
func MeanAbsoluteDeviation(numbers []float64) float64 {
    mean := mean(numbers)
    return average(abs(numbers, mean))
}

func mean(numbers []float64) float64 {
    return sum(numbers) / float64(len(numbers))
}

func sum(numbers []float64) float64 {
    total := 0.0
    for _, num := range numbers {
        total += num
    }
    return total
}

func average(numbers []float64) float64 {
    return sum(numbers) / float64(len(numbers))
}

func abs(numbers []float64, mean float64) []float64 {
    result := make([]float64, len(numbers))
    for i, num := range numbers {
        result[i] = math.Abs(num - mean)
    }
    return result
}
```
