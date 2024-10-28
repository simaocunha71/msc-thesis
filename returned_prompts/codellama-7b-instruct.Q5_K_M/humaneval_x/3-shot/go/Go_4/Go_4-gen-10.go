    mean := Mean(numbers)
    var total float64 = 0

    for _, number := range numbers {
        total += math.Abs(number - mean)
    }

    return total / float64(len(numbers))
}



