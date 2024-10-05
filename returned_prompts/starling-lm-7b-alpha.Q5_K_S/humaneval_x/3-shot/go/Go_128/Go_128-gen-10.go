    if len(arr) == 0 {
        return nil
    }

    result := int64(1)
    for _, v := range arr {
        if v == 0 {
            result *= 0
        }else if v > 0 {
            result *= 1
        }else {
            result *= -1
        }
    }
    return result
}



