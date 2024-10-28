    n := len(s)
    runes := make([]rune, n)
    for _, rune := range s {
        n -= 1
        runes[n] = rune
    }
    return string(runes)
}



