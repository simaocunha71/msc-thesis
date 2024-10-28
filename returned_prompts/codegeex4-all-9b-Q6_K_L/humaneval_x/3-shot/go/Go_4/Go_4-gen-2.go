    var sum float64 = 0
    var mean float64 = 0
    var mad float64 = 0

    for _, number := range numbers{
        sum += number
    }

    mean = sum / float64(len(numbers))

    for _, number := range numbers{
        mad += math.Abs(number - mean)
    }

    return mad / float64(len(numbers))
}



