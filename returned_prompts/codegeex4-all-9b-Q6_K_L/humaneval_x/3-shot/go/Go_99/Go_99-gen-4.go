    number, _ := strconv.ParseFloat(value, 64)
    if number < 0 {
        return int(math.Ceil(number) - 1)
    } else {
        return int(math.Floor(number))
    }
}



