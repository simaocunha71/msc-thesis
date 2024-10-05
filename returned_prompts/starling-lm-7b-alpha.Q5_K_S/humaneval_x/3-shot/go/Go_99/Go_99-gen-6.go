    floatValue, _ := strconv.ParseFloat(value,64)
    if floatValue == math.Floor(floatValue) {
        return int(floatValue)
    }
    if math.Floor(floatValue) + 1 == floatValue {
        return int(math.Floor(floatValue) + 1)
    }
    if floatValue - 1 == math.Floor(floatValue) {
        return int(floatValue - 1)
    }
    return int(math.Ceil(floatValue))
}



