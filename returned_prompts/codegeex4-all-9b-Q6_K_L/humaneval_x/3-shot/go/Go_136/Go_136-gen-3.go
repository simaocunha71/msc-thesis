    var largest_negative int = math.MinInt64
    var smallest_positive int = math.MaxInt64
    var largest_negative_exists bool = false
    var smallest_positive_exists bool = false

    for _, i := range lst {
        if i < 0 {
            if i > largest_negative {
                largest_negative = i
                largest_negative_exists = true
            }
        } else if i > 0 {
            if i < smallest_positive {
                smallest_positive = i
                smallest_positive_exists = true
            }
        }
    }

    if largest_negative_exists && smallest_positive_exists {
        return [2]interface{}{largest_negative, smallest_positive}
    } else if largest_negative_exists {
        return [2]interface{}{largest_negative, nil}
    } else if smallest_positive_exists {
        return [2]interface{}{nil, smallest_positive}
    } else {
        return [2]interface{}{nil, nil}
    }
}


