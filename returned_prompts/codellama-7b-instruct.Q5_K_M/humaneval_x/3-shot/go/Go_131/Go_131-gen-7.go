    result := 0
    for i := 0; i < len(strconv.Itoa(n)); i++ {
        var current_digit, _ = strconv.Atoi(string(strconv.Itoa(n)[i]))
        if current_digit % 2 != 0 {
            result = result * current_digit
        }
    }
    return result
}



