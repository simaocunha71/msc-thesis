    num, _ := strconv.ParseFloat(value, 64)
    if num < 0 {
        return int(math.Ceil(num - 0.5))
    } else {
        return int(math.Ceil(num - 0.5))
    }
}