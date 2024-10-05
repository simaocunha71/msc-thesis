    if len(arr) == 0 {
        return nil
    }
    var sign int = 1
    var sum int = 0
    for _, num := range arr {
        if num < 0 {
            sign *= -1
        }
        sum += int(math.Abs(float64(num)))
    }
    return int64(sign * int64(sum))
}