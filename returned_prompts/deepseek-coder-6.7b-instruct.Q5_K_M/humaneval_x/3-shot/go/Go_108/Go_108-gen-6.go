    counter := 0
    for _, val := range arr {
        sum := 0
        str := strconv.Itoa(val)
        for _, ch := range str {
            if ch == '-' {
                continue
            }
            digit, _ := strconv.Atoi(string(ch))
            sum += digit
        }
        if sum > 0 {
            counter++
        }
    }
    return counter
}



