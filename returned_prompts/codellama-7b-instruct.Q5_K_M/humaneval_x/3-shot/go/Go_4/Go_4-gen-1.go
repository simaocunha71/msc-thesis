    sum := 0.0
    for _, n := range numbers {
        sum += n
    }
    return sum / float64(len(numbers))
}


