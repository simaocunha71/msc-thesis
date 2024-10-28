    result := 1
    for i := 0; i < len(strconv.Itoa(n)); i++ {
        c := strconv.Itoa(n)[i]
        if c%2 != 0 {
            result *= int(c - '0')
        }
    }
    return result
}

