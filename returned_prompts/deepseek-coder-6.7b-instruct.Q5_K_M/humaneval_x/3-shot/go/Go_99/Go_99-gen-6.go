    num, err := strconv.ParseFloat(value, 64)
    if err != nil {
        return 0
    }
    if num >= 0 {
        return int(math.Ceil(num))
    } else {
        return int(math.Floor(num))
    }
}



