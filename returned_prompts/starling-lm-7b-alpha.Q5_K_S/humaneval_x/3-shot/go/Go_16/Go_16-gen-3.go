    str = strings.ToLower(str)
    distinct := make(map[rune]bool)
    for _, c := range str {
        if _, ok := distinct[c]; !ok {
            distinct[c] = true
        }
    }
    return len(distinct)
}



