    mean := 0.0
    for _, n := range numbers {
        mean += n
    }
    mean /= float64(len(numbers))

    sum := 0.0
    for _, n := range numbers {
        sum += math.Abs(n - mean)
    }
    return sum / float64(len(numbers))
}



