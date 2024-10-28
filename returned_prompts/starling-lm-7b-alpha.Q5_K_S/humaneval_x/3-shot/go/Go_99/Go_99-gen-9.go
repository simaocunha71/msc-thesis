    number, _ := strconv.ParseFloat(value, 64)
    int_part := int(math.Floor(number))
    next_int := int_part + 1
    if next_int - number > number - int_part {
        return next_int
    }
    return int_part
}



