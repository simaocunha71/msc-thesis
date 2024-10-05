    mean := 0.0
    for _, number := range numbers {
        mean += number
    }
    mean = mean / float64(len(numbers))

    var sum float64 = 0
    for _, number := range numbers {
        sum += math.Abs(number - mean)
    }
    return sum / float64(len(numbers))
}



