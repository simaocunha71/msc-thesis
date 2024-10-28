    var number float64
    var err error
    number, err = strconv.ParseFloat(value, 64)
    if err != nil {
        panic(err)
    }
    return int(number + math.Copysign(0.5, number))
}

