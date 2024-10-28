    if a == b {
        return nil
    }
    if a_type, ok := a.(float64); ok {
        if b_type, ok := b.(float64); ok {
            if a_type > b_type {
                return a_type
            } else {
                return b_type
            }
        } else if b_str, ok := b.(string); ok {
            if a_type > stringToFloat(b_str) {
                return a_type
            } else {
                return b_type
            }
        } else {
            return b
        }
    } else if a_str, ok := a.(string); ok {
        if b_type, ok := b.(float64); ok {
            if stringToFloat(a_str) > b_type {
                return a_str
            } else {
                return b_type
            }
        } else if b_str, ok := b.(string); ok {
            if stringToFloat(a_str) > stringToFloat(b_str) {
                return a_str
            } else {
                return b_str
            }
        } else {
            return b
        }
    } else {
        return b
    }
}

func stringToFloat(str string) float64 {
    str = strings.Replace(str, ",", "", -1)
    float_str := ""
    for _, c := range str {
        if c == '.' {
            float_str += c
        } else if c >= '0' && c <= '9' {
            float_str += string(c)
        }
    }
    result, _ := strconv.ParseFloat(float_str, 64)
    return result
}



