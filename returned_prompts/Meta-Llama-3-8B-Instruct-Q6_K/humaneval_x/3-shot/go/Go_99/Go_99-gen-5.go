    num, _ := strconv.ParseFloat(value, 64)
    if num-int(num) < 0.5 {
        return int(num)
    } else {
        return int(math.Ceil(num))
    }
}