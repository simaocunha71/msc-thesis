    num, _ := strconv.ParseFloat(value, 64)
    rounded := math.Round(num)
    if math.Abs(rounded-num) == 0.5 {
        return int(rounded) * int(math.Signbit(num))
    }
    return int(rounded)
}



