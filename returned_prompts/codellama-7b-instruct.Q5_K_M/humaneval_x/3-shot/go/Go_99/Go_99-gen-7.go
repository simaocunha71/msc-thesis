    num, _ := strconv.ParseFloat(value, 64)
    sign := 1
    if num < 0 {
        sign = -1
    }
    return int(math.Round(float64(sign)*num-0.5))
}



