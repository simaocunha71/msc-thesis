    result := 1
    is_odd := false
    for _, digit := range strconv.Itoa(n) {
        int_digit, _ := strconv.Atoi(string(digit))
        if int_digit % 2 != 0 {
            is_odd = true
            result *= int_digit
        }
    }
    if !is_odd {
        return 0
    }
    return result
}



