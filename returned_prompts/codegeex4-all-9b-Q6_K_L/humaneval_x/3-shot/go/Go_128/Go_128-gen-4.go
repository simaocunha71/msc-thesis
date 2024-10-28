    if len(arr) == 0{
        return nil
    }
    prod := 1
    sum := 0
    for _, i := range arr{
        prod *= i
        sum += i
    }
    return math.Abs(float64(sum)) * prod
}

