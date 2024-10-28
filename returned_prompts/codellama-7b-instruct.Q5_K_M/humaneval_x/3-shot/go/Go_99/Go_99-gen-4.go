    var result int
    var remainder float64
    var value_int, _ = strconv.Atoi(value)

    if math.Abs(float64(value_int)) < 10 {
        remainder = math.Mod(math.Abs(float64(value_int)), 1)

        if remainder > 0.5 {
            result = value_int + 1
        } else {
            result = value_int
        }

    } else {
        remainder = math.Mod(math.Abs(float64(value_int)), 10)

        if remainder > 5 {
            result = value_int + 10
        } else {
            result = value_int
        }
    }
    return result
}



