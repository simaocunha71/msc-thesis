    if x < base {
        return strconv.Itoa(x)
    }
    result := ""
    for x > 0 {
        x, remainder := divMod(x, base)
        result = strconv.Itoa(remainder) + result
    }
    return result
}

func divMod(dividend int, divisor int) (int, int) {
    return dividend / divisor, dividend % divisor
}