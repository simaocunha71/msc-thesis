    if len(arr) == 0 {
        return nil
    }

    sum  := 0
    prod := 1

    for _, num := range arr {
        if num < 0 {
            prod *= -1
        } else if num > 0 {
            prod *= 1
        }
        sum += int(math.Abs(float64(num)))
    }

    return prod * sum
}



