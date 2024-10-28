    floatValue, err := strconv.ParseFloat(value, 64)
    if err != nil {
        panic(err)
    }
    if floatValue > 0 {
        return int(floatValue + 0.5)
    } else {
        return int(floatValue - 0.5)
    }
}



