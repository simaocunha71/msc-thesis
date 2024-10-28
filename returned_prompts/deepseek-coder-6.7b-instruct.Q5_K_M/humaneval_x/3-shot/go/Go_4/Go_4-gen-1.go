    sum := 0.0
    mean := 0.0
    for _, num := range numbers {
        sum += num
    }
    mean = sum / float64(len(numbers))
    mad := 0.0
    for _, num := range numbers {
        mad += math.Abs(num - mean)
    }
    mad /= float64(len(numbers))
    return mad
}



