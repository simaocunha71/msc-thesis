    mean := Mean(numbers)
    sum := 0.0

    for _, num := range numbers {
        sum += math.Abs(num - mean)
    }

    return sum / float64(len(numbers))
}



