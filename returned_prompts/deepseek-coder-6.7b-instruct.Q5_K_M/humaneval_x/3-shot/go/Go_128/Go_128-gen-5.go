    if len(arr) == 0 {
        return nil
    }
    sumOfMagnitudes := 0
    prodOfSigns := 1
    for _, val := range arr {
        if val < 0 {
            prodOfSigns *= -1
            sumOfMagnitudes += int(math.Abs(float64(val)))
        } else if val > 0 {
            prodOfSigns *= 1
            sumOfMagnitudes += int(math.Abs(float64(val)))
        } else {
            return 0
        }
    }
    return prodOfSigns * sumOfMagnitudes
}



