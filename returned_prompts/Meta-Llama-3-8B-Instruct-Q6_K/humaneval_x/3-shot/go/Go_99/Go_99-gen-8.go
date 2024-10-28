    num, _ := strconv.ParseFloat(value, 64)
    return int(math.Ceil(float64(num)))
}