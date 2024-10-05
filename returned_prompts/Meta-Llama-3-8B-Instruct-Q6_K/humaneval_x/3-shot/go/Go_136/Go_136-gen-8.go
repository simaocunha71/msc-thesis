    var result [2]interface{}
    largest_negative := nil
    smallest_positive := nil

    for _, v := range lst {
        if v < 0 && largest_negative == nil {
            largest_negative = v
        } else if v < 0 && largest_negative != nil && v > largest_negative.(int) {
            largest_negative = v
        }
        if v > 0 && smallest_positive == nil {
            smallest_positive = v
        } else if v > 0 && smallest_positive != nil && v < smallest_positive.(int) {
            smallest_positive = v
        }
    }

    if largest_negative == nil && smallest_positive == nil {
        result[0] = nil
        result[1] = nil
    } else if largest_negative == nil {
        result[0] = nil
        result[1] = smallest_positive
    } else if smallest_positive == nil {
        result[0] = largest_negative
        result[1] = nil
    } else {
        result[0] = largest_negative
        result[1] = smallest_positive
    }

    return result
}