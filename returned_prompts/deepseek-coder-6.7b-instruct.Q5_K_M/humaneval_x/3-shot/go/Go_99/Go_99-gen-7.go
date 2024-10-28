    floatValue, _ := strconv.ParseFloat(value, 64)
    integerPart := math.Floor(floatValue)
    decimalPart := math.Abs(floatValue - integerPart)

    if decimalPart < 0.5 {
        return int(integerPart)
    } else {
        if strings.HasPrefix(value, "-") {
            return int(integerPart) - 1
        } else {
            return int(integerPart) + 1
        }
    }
}



