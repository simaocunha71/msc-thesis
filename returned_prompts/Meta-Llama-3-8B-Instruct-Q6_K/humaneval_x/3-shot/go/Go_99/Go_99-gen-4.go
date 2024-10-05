    num, _ := strconv.ParseFloat(value, 64)
    return int(math.Round(math.Abs(num)))
}