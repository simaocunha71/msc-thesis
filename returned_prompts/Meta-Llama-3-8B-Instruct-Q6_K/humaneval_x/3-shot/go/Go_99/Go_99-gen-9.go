    num, _ := strconv.ParseFloat(value, 64)
    if num < 0 {
        if math.Mod(num, 1) < 0.5 {
            return int(math.Floor(num))
        } else {
            return int(math.Ceil(num))
        }
    } else {
        if math.Mod(num, 1) < 0.5 {
            return int(math.Floor(num))
        } else {
            return int(math.Ceil(num))
        }
    }
}