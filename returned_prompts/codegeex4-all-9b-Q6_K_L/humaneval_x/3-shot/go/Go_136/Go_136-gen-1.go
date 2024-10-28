    largest_negative := math.MinInt64
    smallest_positive := math.MaxInt64

    for _, i := range lst {
        if i < 0 && i > largest_negative {
            largest_negative = i
        }
        if i > 0 && i < smallest_positive {
            smallest_positive = i
        }
    }
    if largest_negative == math.MinInt64 {
        largest_negative = nil
    }
    if smallest_positive == math.MaxInt64 {
        smallest_positive = nil
    }
    return [2]interface{}{largest_negative, smallest_positive}
}