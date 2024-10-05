    var max_negative *int = nil
    var min_positive *int = nil

    for _, num := range lst {
        if num < 0 && (max_negative == nil || num > *max_negative) {
            max_negative = &num
        }
        if num > 0 && (min_positive == nil || num < *min_positive) {
            min_positive = &num
        }
    }

    return [2]interface{}{max_negative, min_positive}
}



