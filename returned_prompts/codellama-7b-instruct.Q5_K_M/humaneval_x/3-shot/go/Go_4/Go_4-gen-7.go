    mean := Mean(numbers)
    sum := 0.0

    for _, x := range numbers {
        sum += math.Abs(x - mean)
    }
    return sum / float64(len(numbers))
}



