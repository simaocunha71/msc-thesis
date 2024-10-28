    mean := meanOfArray(numbers)
    var sum float64 = 0
    for _, num := range numbers {
        sum += math.Abs(num - mean)
    }
    return sum / float64(len(numbers))
}

func meanOfArray(numbers []float64) float64 {
    sum := 0
    for _, num := range numbers {
        sum += num
    }
    return sum / float64(len(numbers))
}