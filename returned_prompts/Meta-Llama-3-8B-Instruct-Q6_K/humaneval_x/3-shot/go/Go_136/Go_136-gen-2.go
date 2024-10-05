    var largest_negative, smallest_positive int
    largest_negative = -math.MaxInt32
    smallest_positive = math.MaxInt32

    for _, val := range lst {
        if val < 0 && val > largest_negative {
            largest_negative = val
        } else if val > 0 && val < smallest_positive {
            smallest_positive = val
        }
    }

    if largest_negative == -math.MaxInt32 {
        largest_negative = nil
    }
    if smallest_positive == math.MaxInt32 {
        smallest_positive = nil
    }

    return [2]interface{}{largest_negative, smallest_positive}
}