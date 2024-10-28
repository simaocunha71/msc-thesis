    words := strings.Fields(s)
    for i := range words {
        chars := []rune(words[i])
        sort.Slice(chars, func(i, j int) bool {
            return chars[i] < chars[j]
        })
        words[i] = string(chars)
    }
    return strings.Join(words, " ")
}



