    words := strings.Split(s, " ")
    for i, word := range words {
        sorted := make([]rune, len(word))
        copy(sorted, word)
        sort.Slice(sorted, func(i, j int) bool {
            return sorted[i] < sorted[j]
        })
        words[i] = string(sorted)
    }
    return strings.Join(words, " ")
}



