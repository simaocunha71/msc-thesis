    numerator_x, _ := strconv.Atoi(strings.Split(x, "/")[0])
    denominator_x, _ := strconv.Atoi(strings.Split(x, "/")[1])
    numerator_n, _ := strconv.Atoi(strings.Split(n, "/")[0])
    denominator_n, _ := strconv.Atoi(strings.Split(n, "/")[1])

    if numerator_x * denominator_n == numerator_n * denominator_x {
        return true
    }
    return false
}



