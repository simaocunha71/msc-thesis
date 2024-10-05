    if len(arr)==0 {
        return nil
    }

    sum,prod := 0,1
    for _, v := range arr {
        if v > 0 {
            prod *= 1
            sum += int(math.Abs(float64(v)))
        } else if v < 0 {
            prod *= -1
            sum += int(math.Abs(float64(v)))
        } else {
            return 0
        }
    }
    return prod*sum
}



