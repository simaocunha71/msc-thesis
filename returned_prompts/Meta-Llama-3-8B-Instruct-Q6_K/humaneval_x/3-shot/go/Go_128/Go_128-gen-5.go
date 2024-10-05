    if len(arr) == 0 {
        return nil
    }

    var sum float64 = 0
    var product int = 1
    for _, num := range arr {
        sum += float64(abs(num))
        if num > 0 {
            product *= 1
        } else if num < 0 {
            product *= -1
        }
    }
    return product * sum
}

func abs(n int) int {
    if n < 0 {
        return -n
    }
    return n
}