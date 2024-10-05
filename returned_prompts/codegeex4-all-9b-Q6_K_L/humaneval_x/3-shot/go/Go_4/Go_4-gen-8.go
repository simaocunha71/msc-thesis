    var sum float64 = 0.0
    for _, num := range numbers{
        sum += num
    }
    mean := sum / float64(len(numbers))

    var sum_dev float64 = 0.0
    for _, num := range numbers{
        sum_dev += math.Abs(num - mean)
    }
    mad := sum_dev / float64(len(numbers))
    return mad
}



