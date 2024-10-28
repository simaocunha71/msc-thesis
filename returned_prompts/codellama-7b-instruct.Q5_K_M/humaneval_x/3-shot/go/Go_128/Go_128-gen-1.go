    var result int
    var product int
    var isNegative bool = false

    if len(arr) == 0 {
        return nil
    }
    for _, num := range arr {

        if num < 0 {
            isNegative = true
        }
        product *= num
    }

    if isNegative {
        result = -product
    } else {
        result = product
    }
    return result
}



