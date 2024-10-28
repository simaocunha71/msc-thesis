    number, err := strconv.ParseFloat(value, 64)
    if err != nil {
        return -1
    }

    var result int
    if number == math.Floor(number) {
        result = int(number)
    } else {
        if number < 0 {
            result = int(math.Ceil(number))
        } else {
            result = int(math.Floor(number))
        }
    }

    return result
}



