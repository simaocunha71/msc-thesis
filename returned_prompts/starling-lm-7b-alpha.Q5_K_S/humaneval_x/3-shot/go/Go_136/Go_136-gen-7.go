    result := [2]interface{}{nil, nil}

    for _, i := range lst {
        if i < 0 {
            if result[0] == nil {
                result[0] = i
            } else if i > result[0] {
                result[0] = i
            }
        }
        if i > 0 {
            if result[1] == nil {
                result[1] = i
            } else if i < result[1] {
                result[1] = i
            }
        }
    }
    return result
}



