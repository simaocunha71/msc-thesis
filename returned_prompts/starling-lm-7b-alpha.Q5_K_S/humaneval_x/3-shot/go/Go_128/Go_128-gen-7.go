    if len(arr) == 0 {
        return nil
    }

    result := 0
    product := 1

    for _, n := range arr {
        if n == 0 {
            result = 0
            product = 1
        } else if n < 0 {
            result += product * -n
            product *= -1
        } else {
            result += product * n
            product *= 1
        }
    }

    return result
}



