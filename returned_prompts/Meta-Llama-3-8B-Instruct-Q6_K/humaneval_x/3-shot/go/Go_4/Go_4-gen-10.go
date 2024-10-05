    mean := calculateMean(numbers)
    deviation := 0.0
    for _, n := range numbers {
        deviation += math.Abs(n - mean)
    }
    return deviation / float64(len(numbers))
}

func calculateMean(numbers []float64) float64 {
    sum := 0.0
    for _, n := range numbers {
        sum += n
    }
    return sum / float64(len(numbers))
}