    sum_of_deviation := 0.0
    for _, number := range numbers {
        sum_of_deviation += math.Abs(number - mean(numbers))
    }
    return sum_of_deviation / float64(len(numbers))
}

func mean(numbers []float64) float64 {
    sum := 0.0
    for _, number := range numbers {
        sum += number
    }
    return sum / float64(len(numbers))
}



