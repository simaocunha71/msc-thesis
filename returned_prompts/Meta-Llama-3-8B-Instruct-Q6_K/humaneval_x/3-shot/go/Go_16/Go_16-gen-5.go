    str = strings.ToLower(str)
    runes := []rune(str)
    m := make(map[rune]bool)
    for _, rune := range runes {
        m[rune] = true
    }
    return len(m)
}