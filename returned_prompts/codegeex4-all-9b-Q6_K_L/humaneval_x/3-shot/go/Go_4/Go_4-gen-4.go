    mean := Mean(numbers)

    total := 0.0
    for _, num := range numbers {
        total += math.Abs(num - mean)
    }
    return total / float64(len(numbers))
}

func Mean(numbers []float64) float64 {
    total := 0.0
    for _, num := range numbers {
        total += num
    }
    return total / float64(len(numbers))
}

