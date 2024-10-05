    result := [2]interface{}{}
    neg_int := math.MinInt32
    pos_int := math.MaxInt32

    for _, v := range lst {
        if v > 0 {
            if v < pos_int {
                pos_int = v
            }
        }else if v < 0 {
            if v > neg_int {
                neg_int = v
            }
        }
    }
    if neg_int != math.MinInt32 {
        result[0] = neg_int
    }
    if pos_int != math.MaxInt32 {
        result[1] = pos_int
    }
    return result
}



