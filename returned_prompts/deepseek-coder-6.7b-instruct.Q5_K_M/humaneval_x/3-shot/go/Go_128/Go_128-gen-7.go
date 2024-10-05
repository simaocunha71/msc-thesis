    if len(arr) == 0 {
        return nil
    }

    sumOfMagnitudes := 0
    productOfSigns := 1

    for _, num := range arr {
        sumOfMagnitudes += int(math.Abs(float64(num)))
        if num < 0 {
            productOfSigns *= -1
        } else if num > 0 {
            productOfSigns *= 1
        } else {
            productOfSigns = 0
            break
        }
    }

    return sumOfMagnitudes * productOfSigns
}



