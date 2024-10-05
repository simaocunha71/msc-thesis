    mean := Mean(numbers)
    mad := 0.0
    for _, v := range numbers {
        mad += math.Abs(v - mean)
    }
    return mad / float64(len(numbers))
}



