    if len(arr) == 0 {
        return nil
    }

    var result int = 0
    var sign int = 1

    for _, value := range arr {
        if value < 0 {
            sign *= -1
        } else if value > 0 {
            sign *= 1
        } else {
            return 0
        }

        result += int(math.Abs(float64(value)))
    }

    return result * sign
}



