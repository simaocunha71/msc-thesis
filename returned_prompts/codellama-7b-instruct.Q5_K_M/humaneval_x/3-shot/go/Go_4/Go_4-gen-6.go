    sum := 0.0
    average := Mean(numbers)

    for _, number := range numbers {
        sum += math.Abs(number - average)
    }

    return sum / float64(len(numbers))
}



