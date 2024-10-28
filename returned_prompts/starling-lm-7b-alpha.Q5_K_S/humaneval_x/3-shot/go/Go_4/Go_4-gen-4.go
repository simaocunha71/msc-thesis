    mean := Mean(numbers)
    var result float64 = 0
    for _, n := range numbers {
        result += math.Abs(n - mean)
    }
    return result / float64(len(numbers))
}



