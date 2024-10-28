    var largest_negative, smallest_positive interface{}
    var largest_negative_found, smallest_positive_found bool

    for _, val := range lst {
        if val < 0 {
            if largest_negative_found {
                largest_negative = math.MaxFloat64
            } else {
                largest_negative = val
                largest_negative_found = true
            }
        } else if val > 0 {
            if smallest_positive_found {
                smallest_positive = 0
            } else {
                smallest_positive = val
                smallest_positive_found = true
            }
        }
    }

    if largest_negative_found && !smallest_positive_found {
        return [2]interface{}{largest_negative, nil}
    } else if !largest_negative_found && smallest_positive_found {
        return [2]interface{}{nil, smallest_positive}
    } else if largest_negative_found && smallest_positive_found {
        return [2]interface{}{largest_negative, smallest_positive}
    } else {
        return [2]interface{}{nil, nil}
    }
}