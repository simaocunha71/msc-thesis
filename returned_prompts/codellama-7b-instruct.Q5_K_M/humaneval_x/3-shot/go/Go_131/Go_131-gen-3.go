    result := 0
    for _, c := range strconv.Itoa(n) {
        if string(c)%2 == 1 {
            result *= int(c - '0')
        }
    }
    return result
}



