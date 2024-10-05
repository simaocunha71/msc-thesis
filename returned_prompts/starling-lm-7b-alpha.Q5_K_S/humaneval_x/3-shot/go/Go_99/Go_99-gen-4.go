    number, _ := strconv.ParseFloat(value, 64)
    closest_int := math.Floor(number)
    if math.Abs(number - closest_int) == math.Abs(closest_int + 1 - number) {
        closest_int += math.Copysign(1, number)
    }
    return int(closest_int)
}



