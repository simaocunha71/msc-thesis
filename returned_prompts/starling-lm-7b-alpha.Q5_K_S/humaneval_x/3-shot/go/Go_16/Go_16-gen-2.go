    str = strings.ToLower(str)
    distinct_chars := make(map[rune]bool)
    for _, c := range str {
        distinct_chars[c] = true
    }
    return len(distinct_chars)
}



