    result := 1
    str_n := strconv.Itoa(n)
    for _, c := range str_n {
        digit, _ := strconv.Atoi(string(c))
        if digit % 2 != 0 {
            result *= digit
        }
    }
    return result
}



