    numerator_x, denominator_x := strconv.ParseFloat(strings.Split(x, "/")[0], 64), strconv.ParseFloat(strings.Split(x, "/")[1], 64)
    numerator_n, denominator_n := strconv.ParseFloat(strings.Split(n, "/")[0], 64), strconv.ParseFloat(strings.Split(n, "/")[1], 64)

    result_numerator := numerator_x * numerator_n
    result_denominator := denominator_x * denominator_n

    result := result_numerator / result_denominator

    return math.Mod(result, 1) == 0
}