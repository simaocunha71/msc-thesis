    var largest_negative, smallest_positive *int
    for _, v := range lst {
        if v < 0 {
            if largest_negative == nil || v > *largest_negative {
                largest_negative = &v
            }
        } else if v > 0 {
            if smallest_positive == nil || v < *smallest_positive {
                smallest_positive = &v
            }
        }
    }
    if largest_negative != nil && smallest_positive != nil {
        return [2]interface{}{largest_negative, smallest_positive}
    }
    return [2]interface{}{nil, nil}
}