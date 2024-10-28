    result := [2]interface{}{nil, nil}
    for _, v := range lst {
        if v < 0 && result[0] == nil {
            result[0] = v
        }
        if v > 0 && result[1] == nil {
            result[1] = v
        }
    }
    return result
}



