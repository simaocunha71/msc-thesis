    var largest_negative, smallest_positive interface{}
    for _, num := range lst {
        if num < 0 {
            largest_negative = num
        } else if num > 0 {
            if smallest_positive == nil || num < smallest_positive.(int) {
                smallest_positive = num
            }
        }
    }
    if largest_negative != nil && smallest_positive != nil {
        return [2]interface{}{largest_negative, smallest_positive}
    }
    if largest_negative != nil {
        return [2]interface{}{largest_negative, nil}
    }
    if smallest_positive != nil {
        return [2]interface{}{nil, smallest_positive}
    }
    return [2]interface{}{nil, nil}
}