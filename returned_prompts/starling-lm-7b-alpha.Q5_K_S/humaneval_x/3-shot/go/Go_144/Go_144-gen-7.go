    numerator_x, denominator_x := simplifyFraction(x)
    numerator_n, denominator_n := simplifyFraction(n)

    result := numerator_x * numerator_n
    denominator_result := denominator_x * denominator_n

    if result % denominator_result == 0 {
        return true
    }
    return false
}

func simplifyFraction(fraction string) (int, int) {
    parts := strings.Split(fraction,"/")
    numerator, _ := strconv.Atoi(parts[0])
    denominator, _ := strconv.Atoi(parts[1])

    while numerator != 0 && denominator != 0 {
        if numerator > denominator {
            dividend := numerator % denominator
            numerator = denominator
            denominator = dividend
        }else if numerator < denominator {
            dividend := denominator % numerator
            denominator = numerator
            numerator = dividend
        }else {
            numerator = 0
            denominator = 0
        }
    }
    return numerator, denominator
}



