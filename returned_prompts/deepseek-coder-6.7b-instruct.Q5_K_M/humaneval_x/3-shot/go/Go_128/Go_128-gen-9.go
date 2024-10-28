    if len(arr) == 0 {
        return nil
    }

    sum := 0
    sign := 1

    for _, num := range arr {
        if num < 0 {
            sign *= -1
            num = -num
        } else if num > 0 {
            sign *= 1
        } else {
            return 0
        }
        sum += num
    }

    return sign * sum
}



