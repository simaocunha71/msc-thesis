    var prod_sign float64 = 1
    var sum float64 = 0
    if len(arr) == 0{
        return nil
    }
    for _, v := range arr {
        prod_sign *= float64(math.Signbit(float64(v)))
        sum += float64(math.Abs(float64(v)))
    }
    return prod_sign * sum
}



