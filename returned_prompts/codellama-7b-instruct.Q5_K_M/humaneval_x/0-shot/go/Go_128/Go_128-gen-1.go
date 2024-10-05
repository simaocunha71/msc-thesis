    if len(arr) == 0 {
        return nil
    }
    var sum int
    var prod int
    var sign int = 1
    for _, v := range arr {
        if v == 0 {
            prod = 0
            sum += sign * v
        } else {
            prod *= sign
            sign = v
            sum += sign * v
        }
    }
    return prod * sum
}
