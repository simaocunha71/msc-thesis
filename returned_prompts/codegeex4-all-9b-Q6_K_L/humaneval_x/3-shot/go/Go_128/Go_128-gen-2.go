    if len(arr) == 0 {
        return nil
    }
    var prodSign int = 1
    var sumOfMagnitudes int = 0
    for _, num := range arr {
        if num < 0 {
            prodSign *= -1
        } else if num == 0 {
            prodSign = 0
        }
        sumOfMagnitudes += int(math.Abs(float64(num)))
    }
    return float64(prodSign) * float64(sumOfMagnitudes)
}