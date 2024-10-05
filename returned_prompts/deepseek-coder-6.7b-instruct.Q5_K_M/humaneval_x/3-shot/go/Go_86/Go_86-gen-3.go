    words := strings.Fields(s)
    for i, word := range words {
        sorted := []rune(word)
        sort.Slice(sorted, func(i, j int) bool {
            return sorted[i] < sorted[j]
        })
        words[i] = string(sorted)
    }
    return strings.Join(words, " ")
}



