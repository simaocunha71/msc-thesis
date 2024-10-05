    mean := Mean(numbers)
    sum_abs_diff := 0.0
    for _, x := range numbers {
        sum_abs_diff += math.Abs(x - mean)
    }
    return sum_abs_diff / float64(len(numbers))
}



