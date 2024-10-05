    var max_negative int = math.MinInt64
    var min_positive int = math.MaxInt64
    var flag bool = false

    for _, num := range lst {
        if num < 0 && num > max_negative {
            max_negative = num
            flag = true
        } else if num > 0 && num < min_positive {
            min_positive = num
            flag = true
        }
    }

    if !flag {
        return [2]interface{}{nil, nil}
    }

    return [2]interface{}{max_negative, min_positive}
}



