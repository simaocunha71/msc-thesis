    if len(arr) == 0 {
        return nil
    }
    
    sum := 0
    sign := 1
    for _, num := range arr {
        if num < 0 {
            sign *= -1
            sum += int(math.Abs(float64(num)))
        } else if num > 0 {
            sign *= 1
            sum += num
        } else {
            return 0
        }
    }
    return sum * sign
}



