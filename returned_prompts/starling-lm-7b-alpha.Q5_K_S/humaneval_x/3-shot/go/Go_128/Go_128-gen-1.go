    if len(arr) == 0 {
        return nil
    }
    result := 0
    sign := 1
    for _, v := range arr {
        sign *= v
        if sign == 0 {
            result = 0
            break
        }
        if sign > 0 {
            result += v
        }else if sign < 0 {
            result -= v
        }
    }
    return result
}



