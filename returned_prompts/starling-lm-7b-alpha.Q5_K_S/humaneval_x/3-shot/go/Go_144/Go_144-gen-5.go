    numerator_x, denominator_x, _ := strconv.ParseInt(strings.Split(x, "/")[0], 10, 64),
        strconv.ParseInt(strings.Split(x, "/")[1], 10, 64), 0
    numerator_n, denominator_n, _ := strconv.ParseInt(strings.Split(n, "/")[0], 10, 64),
        strconv.ParseInt(strings.Split(n, "/")[1], 10, 64), 0

    if (numerator_n*denominator_x)%denominator_n == 0 {
        return true
    }
    return false
}



