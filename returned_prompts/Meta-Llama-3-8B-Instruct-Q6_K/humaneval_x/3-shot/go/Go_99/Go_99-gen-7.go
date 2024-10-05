    num, _ := strconv.ParseFloat(value, 64)
    if num > 0 {
        return int(math.Ceil(num))
    } else {
        return int(math.Floor(num))
    }
}