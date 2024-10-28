    result := [2]interface{}{nil, nil}
    positive_ints := make([]int, 0)
    negative_ints := make([]int, 0)
    for _, v := range lst {
        if v > 0 {
            positive_ints = append(positive_ints, v)
        }else if v < 0 {
            negative_ints = append(negative_ints, v)
        }
    }
    if len(positive_ints) != 0 {
        result[1] = min(positive_ints)
    }
    if len(negative_ints) != 0 {
        result[0] = max(negative_ints)
    }
    return result
}



