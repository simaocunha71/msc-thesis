    str = strings.ToLower(str)
    m := make(map[rune]bool)
    for _, char := range str {
        m[char] = true
    }
    return len(m)
}



