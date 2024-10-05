    number, err := strconv.ParseFloat(value,64)
    if err != nil {
        panic(err)
    }
    return int(math.Ceil(number))
}



