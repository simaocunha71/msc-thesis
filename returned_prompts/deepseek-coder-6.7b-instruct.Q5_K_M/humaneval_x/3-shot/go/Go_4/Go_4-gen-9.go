    var sum float64 = 0
    var mean float64
    var mad float64 = 0

    for i := 0; i < len(numbers); i++ {
        sum += numbers[i]
    }

    mean = sum / float64(len(numbers))

    for i := 0; i < len(numbers); i++ {
        mad += math.Abs(numbers[i] - mean)
    }

    return mad / float64(len(numbers))
}



