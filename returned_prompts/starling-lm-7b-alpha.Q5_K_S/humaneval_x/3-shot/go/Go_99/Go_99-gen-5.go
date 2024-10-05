    number, err := strconv.ParseFloat(value, 64)

    if err != nil {
        return 0
    }

    if number == math.Floor(number) {
        return int(number)
    }

    if number < 0 {
        return int(math.Ceil(number))
    }else {
        return int(math.Floor(number))
    }
}



