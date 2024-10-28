    mean := mean(numbers)
    return abs(sub(numbers, mean)).mean()
}

func mean(numbers []float64) float64 {
    sum := 0.0
    for _, v := range numbers {
        sum += v
    }
    return sum / float64(len(numbers))
}

func abs(v float64) float64 {
    return math.Abs(v)
}

func sub(numbers []float64, v float64) []float64 {
    result := make([]float64, len(numbers))
    for i, n := range numbers {
        result[i] = n - v
    }
    return result
}

func mean(numbers []float64) float64 {
    sum := 0.0
    for _, v := range numbers {
        sum += v
    }
    return sum / float64(len(numbers))
}



