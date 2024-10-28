    if len(arr) == 0 {
        return nil
    }
    result := int64(1)
    product := int64(1)
    for _, v := range arr {
        if v == 0 {
            product *= v
        }else if v < 0 {
            product *= -1
        }else {
            result *= v
        }
    }
    return int64(result) * product
}



