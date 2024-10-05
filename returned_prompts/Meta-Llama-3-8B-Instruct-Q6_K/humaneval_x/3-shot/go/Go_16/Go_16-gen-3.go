    str = strings.ToLower(str)
    charSet := make(map[rune]bool)
    for _, char := range str {
        if _, value := charSet[char]; !value {
            charSet[char] = true
        }
    }
    return len(charSet)
}