    mean := 0.0
    for _, num := range numbers {
        mean += num
    }
    mean /= float64(len(numbers))

    var mad float64
    for _, num := range numbers {
        mad += math.Abs(num - mean)
    }
    mad /= float64(len(numbers))
    return mad
}