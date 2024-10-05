    words := strings.Split(s, " ")
    var result []string
    for _, word := range words {
        word_runes := []rune(word)
        sort.Slice(word_runes, func(i, j int) bool {
            return word_runes[i] < word_runes[j]
        })
        result = append(result, string(word_runes))
    }
    return strings.Join(result, " ")
}



