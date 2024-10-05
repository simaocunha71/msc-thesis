    floatValue, _ := strconv.ParseFloat(value, 64)
    if math.Abs(floatValue) < 0.5 {
        return 0
    }
    return int(math.Ceil(floatValue))
}



