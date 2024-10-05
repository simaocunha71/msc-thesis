    result := [2]interface{}{nil,nil}

    if len(lst) == 0 {
        return result
    }

    isNegative := false
    for _, v := range lst {
        if v < 0 {
            if result[0] == nil {
                result[0] = v
            } else {
                if v > result[0] {
                    result[0] = v
                }
            }
            isNegative = true
        } else if v > 0 && result[1] == nil {
            result[1] = v
        }
    }

    if isNegative {
        result[0] = int(result[0].(float64))
    }
    result[1] = int(result[1].(float64))

    return result
}



