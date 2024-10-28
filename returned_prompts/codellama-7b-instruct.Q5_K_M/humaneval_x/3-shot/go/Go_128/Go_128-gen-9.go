    if len(arr) == 0 {
        return nil
    }
    var result int = 1
    var product int = 1
    for _, v := range arr {
        product *= v
        result += math.Abs(product)
    }
    return result
}



