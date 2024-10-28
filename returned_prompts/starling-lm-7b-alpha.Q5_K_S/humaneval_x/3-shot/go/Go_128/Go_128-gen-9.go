    if len(arr) == 0 {
        return nil
    }
    var sign int = 1
    var result int64 = 0
    for _, v := range arr {
        if v == 0 {
            sign = 0
        } else if v > 0 {
            sign = 1
        } else {
            sign = -1
        }
        result += int64(math.Abs(float64(v)) * float64(sign))
    }
    return result
}



