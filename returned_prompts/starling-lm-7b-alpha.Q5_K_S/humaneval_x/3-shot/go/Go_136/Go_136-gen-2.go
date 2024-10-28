    result := [2]interface{}{nil, nil}
    for _, v := range lst {
        if v < 0 {
            if result[0] == nil || v > result[0].(int) {
                result[0] = v
            }
        }else if v > 0 {
            if result[1] == nil || v < result[1].(int) {
                result[1] = v
            }
        }
    }
    return result
}



