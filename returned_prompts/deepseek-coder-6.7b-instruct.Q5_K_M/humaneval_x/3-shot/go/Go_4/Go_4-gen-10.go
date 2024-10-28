    var sum float64 = 0.0
    var mean float64 = Mean(numbers)
    for _, num := range numbers {
        sum += math.Abs(num - mean)
    }
    return sum / float64(len(numbers))
}

func Mean(numbers  []float64) float64  {
    var sum float64 = 0.0
    for _, num := range numbers {
        sum += num
    }
    return sum / float64(len(numbers))
}



