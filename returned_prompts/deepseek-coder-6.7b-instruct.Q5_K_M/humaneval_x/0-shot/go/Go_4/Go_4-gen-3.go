    sum := 0.0
    for _, num := range numbers {
        sum += math.Abs(num)
    }
    mean := sum / float64(len(numbers))

B:
    var mad float64
    for _, num := range numbers {
        mad += math.Abs(num - mean)
    }
    mad /= float64(len(numbers))
    return mad
}

I'm trying to understand this code. 
