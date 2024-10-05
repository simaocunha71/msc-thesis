    words := strings.Fields(s)
    for i, word := range words {
        runes := []rune(word)
        sort.Slice(runes, func(i, j int) bool {
            return runes[i] < runes[j]
        })
        words[i] = string(runes)
    }
    return strings.Join(words, " ")
}



