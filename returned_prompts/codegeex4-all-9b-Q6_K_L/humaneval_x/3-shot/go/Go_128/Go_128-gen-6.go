    var prodSign int
    sum := 0
    for _, v := range arr {
        if v < 0 {
            prodSign = -1
        } else if v == 0 {
            prodSign = 0
        } else {
            prodSign = 1
        }
        sum += math.Abs(float64(v)) * float64(prodSign)
    }
    return sum
}



