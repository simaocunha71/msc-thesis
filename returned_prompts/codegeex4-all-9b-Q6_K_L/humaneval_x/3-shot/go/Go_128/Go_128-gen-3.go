    if len(arr) == 0 {
        return nil
    }

    var product int = 1
    var sum int = 0

    for _, v := range arr {
        product *= v / math.Abs(float64(v))
        sum += math.Abs(float64(v))
    }

    return product * sum
}

