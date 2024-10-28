    mean := 0.0
    sum := 0.0
    for _, num := range numbers {
        mean += num
        sum += math.Abs(num - (mean / float64(len(numbers))))
    }
    return sum / float64(len(numbers))
}  // or 
    return math.Abs(mean - float64(sum) / float64(len(numbers)))  // if you want to calculate mean first

