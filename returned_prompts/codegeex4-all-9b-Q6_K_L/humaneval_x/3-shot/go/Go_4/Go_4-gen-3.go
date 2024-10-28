    mean := 0.0
    for _, num := range numbers {
        mean += num
    }
    mean /= float64(len(numbers))

    var sum float64 = 0.0
    for _, num := range numbers {
        sum += math.Abs(num - mean)
    }
    return sum / float64(len(numbers))
}



