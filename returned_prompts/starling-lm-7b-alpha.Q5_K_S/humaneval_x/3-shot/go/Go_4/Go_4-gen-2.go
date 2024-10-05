    mean := 0.0
    for _, n := range numbers {
        mean += n
    }
    mean /= float64(len(numbers))

    result := 0.0
    for _, n := range numbers {
        result += math.Abs(n - mean)
    }
    return result / float64(len(numbers))
}



