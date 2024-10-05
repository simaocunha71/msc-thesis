    mean := Mean(numbers)
    deviation_sum := 0.0

    for _, number := range numbers {
        deviation := math.Abs(number - mean)
        deviation_sum += deviation
    }

    return deviation_sum / float64(len(numbers))
}



