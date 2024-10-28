    str = strings.ToLower(str)
    charSet := make(map[rune]bool)
    for _, val := range str {
        charSet[val] = true
    }
    return len(charSet)
}