    if len(arr) == 0 {
        return nil
    }

    result := 0
    for _, v := range arr {
        if v == 0 {
            continue
        }
        if v > 0 {
            result += v
        }else{
            result -= v
        }
    }
    return result
}



