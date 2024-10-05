    if len(arr)==0 {
        return nil
    }

    var sign_product int = 1
    var magnitude_sum int = 0

    for _, v := range arr {
        var sign int
        if v < 0 {
            sign = -1
        } else if v > 0 {
            sign = 1
        } else {
            sign = 0
        }

        sign_product = sign_product * sign
        magnitude_sum += math.Abs(v)
    }

    return sign_product * magnitude_sum
}



