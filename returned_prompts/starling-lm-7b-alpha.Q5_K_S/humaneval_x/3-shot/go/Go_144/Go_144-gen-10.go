    numerator_x, denominator_x := parseFraction(x)
    numerator_n, denominator_n := parseFraction(n)

    numerator_result := numerator_x * numerator_n
    denominator_result := denominator_x * denominator_n

    gcd := GCD(numerator_result, denominator_result)

    if gcd == 1 {
        return true
    }else {
        return false
    }
}

func GCD(a, b int) int {
    for b != 0 {
        temp := a % b
        a = b
        b = temp
    }
    return a
}

func parseFraction(str string) (int, int) {
    parts := strings.Split(str, "/")
    numerator, _ := strconv.Atoi(parts[0])
    denominator, _ := strconv.Atoi(parts[1])
    return numerator, denominator
}



