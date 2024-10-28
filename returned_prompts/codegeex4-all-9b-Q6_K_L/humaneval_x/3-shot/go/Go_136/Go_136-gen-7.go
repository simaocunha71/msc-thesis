    var largest_negative int
    var smallest_positive int
    var is_largest_negative_found bool
    var is_smallest_positive_found bool

    for _, x := range lst {
        if x < 0 {
            if !is_largest_negative_found || x > largest_negative {
                is_largest_negative_found = true
                largest_negative = x
            }
        } else if x > 0 {
            if !is_smallest_positive_found || x < smallest_positive {
                is_smallest_positive_found = true
                smallest_positive = x
            }
        }
    }
    if !is_largest_negative_found {
        largest_negative = 0
    }
    if !is_smallest_positive_found {
        smallest_positive = 0
    }
    return [2]interface{}{largest_negative, smallest_positive}
}