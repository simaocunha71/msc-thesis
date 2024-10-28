    var largest_smallest [2]interface{}
    max_negative := math.MinInt64
    min_positive := math.MaxInt64

    for _, num := range lst {
        if num < 0 && num > max_negative {
            max_negative = num
        } else if num > 0 && num < min_positive {
            min_positive = num
        }
    }

    if max_negative == math.MinInt64 {
        largest_smallest[0] = nil
    } else {
        largest_smallest[0] = max_negative
    }

    if min_positive == math.MaxInt64 {
        largest_smallest[1] = nil
    } else {
        largest_smallest[1] = min_positive
    }

    return largest_smallest
}