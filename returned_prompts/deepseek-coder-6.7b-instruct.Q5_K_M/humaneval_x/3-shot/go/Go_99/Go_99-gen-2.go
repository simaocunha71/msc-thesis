    floatValue, _ := strconv.ParseFloat(value, 64)
    intPart := math.Floor(floatValue)
    decimalPart := math.Abs(floatValue - intPart)
    if decimalPart < 0.5 {
        return int(intPart)
    } else if floatValue < 0 {
        return int(intPart) - 1
    } else {
        return int(intPart) + 1
    }
}



