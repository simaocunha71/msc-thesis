    float, err := strconv.ParseFloat(value, 64)
    if err != nil {
        return 0
    }

    if float == math.Trunc(float) {
        return int(float)
    }

    if float > 0 {
        return int(math.Ceil(float))
    } else {
        return int(math.Floor(float))
    }
}



