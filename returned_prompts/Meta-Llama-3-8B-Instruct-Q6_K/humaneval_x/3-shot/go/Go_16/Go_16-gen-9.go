    str = strings.ToLower(str)
    charSet := make(map[rune]bool)
    for _, char := range str {
        charSet[char] = true
    }
    return len(charSet)
}