    str = strings.ToLower(str)
    char_count := make(map[rune]int)
    for _, c := range str {
        char_count[c]++
    }
    return len(char_count)
}