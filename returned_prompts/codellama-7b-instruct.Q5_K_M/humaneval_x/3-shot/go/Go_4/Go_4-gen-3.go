    mean := Mean(numbers)
    sum := 0.0
    for _, v := range numbers {
        sum += math.Abs(v - mean)
    }
    return sum / float64(len(numbers))
}



