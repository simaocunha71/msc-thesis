    var sum float64 = 0.0
    var mean float64 = 0.0

    for _, num := range numbers {
        sum += num
    }

    mean = sum / float64(len(numbers))

    sum = 0.0

    for _, num := range numbers {
        sum += math.Abs(num - mean)
    }

    return sum / float64(len(numbers))
}



