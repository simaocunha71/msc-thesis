    mean := Mean(numbers)
    result := 0.0
    for _, number := range numbers {
        result += math.Abs(mean - number)
    }
    return result / float64(len(numbers))
}



