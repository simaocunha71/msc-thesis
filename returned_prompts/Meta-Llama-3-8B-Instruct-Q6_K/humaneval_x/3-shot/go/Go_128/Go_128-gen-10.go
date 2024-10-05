    if len(arr) == 0 {
        return nil
    }

    var prodSigns int = 1
    var sumMag int = 0

    for _, num := range arr {
        if num == 0 {
            return 0
        }
        prodSigns *= math.Signum(float64(num))
        sumMag += math.Abs(float64(num))
    }

    return int64(sumMag * float64(prodSigns))
}  // or return float64(sumMag * float64(prodSigns)) if you want to return float instead of int.  // or return int(sumMag * prodSigns) if you want to return int instead of int64.