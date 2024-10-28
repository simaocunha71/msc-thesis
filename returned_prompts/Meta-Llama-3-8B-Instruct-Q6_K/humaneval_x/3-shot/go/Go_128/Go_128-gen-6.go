    var product int
    var sum int
    if len(arr) == 0 {
        return nil
    }
    for _, num := range arr {
        if num > 0 {
            product *= 1
            sum += num
        } else if num < 0 {
            product *= -1
            sum -= num
        } else {
            if product == 0 {
                product = 1
            }
        }
    }
    return sum * product
}  // Use the interface{} type to return nil in case of an empty array. This is a common pattern in Go.