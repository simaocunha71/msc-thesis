    if len(arr) == 0{
        return nil
    }

    var product int = 1
    var sum int = 0
    for _, num := range arr{
        product *= math.Signbit(float64(num))
        sum += math.Abs(float64(num))
    }
    return product * sum
}



