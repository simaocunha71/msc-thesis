    if len(arr) == 0 {
        return nil
    }

    var sum int = 0
    var product int = 1
    for _, num := range arr {
        if num == 0 {
            product *= 0
        } else if num > 0 {
            product *= 1
            sum += num
        } else {
            product *= -1
            sum += -num
        }
    }
    return product*sum
}



