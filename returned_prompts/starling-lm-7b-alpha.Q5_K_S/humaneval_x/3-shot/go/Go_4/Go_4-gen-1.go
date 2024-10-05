    var sum_abs_deviation float64 = 0
    var sum_numbers float64 = 0.0
    var count int = 0
    for _, num := range numbers {
        sum_numbers += num
        count ++
    }

    mean := sum_numbers / float64(count)
    for _, num := range numbers {
        sum_abs_deviation += math.Abs(num - mean)
    }
    return sum_abs_deviation / float64(count)
}



