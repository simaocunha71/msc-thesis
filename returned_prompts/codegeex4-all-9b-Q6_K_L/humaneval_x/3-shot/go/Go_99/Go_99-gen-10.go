    number, err := strconv.ParseFloat(value,64)
    if err != nil {
        return 0
    }
    return int(math.Round(number))
}



