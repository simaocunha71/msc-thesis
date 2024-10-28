    sum  := 0.0
    mean  := 0.0
    for _, number := range numbers {
        sum += number
    }
    mean = sum / float64(len(numbers))

    deviation_sum := 0.0
    for _, number := range numbers {
        deviation_sum += math.Abs(number - mean)
    }

    return deviation_sum / float64(len(numbers))
}



