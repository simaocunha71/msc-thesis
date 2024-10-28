    words := strings.Fields(s)
    sorted_words := make([]string, len(words))

    for i, word := range words {
        sorted_word := make([]rune, len(word))
        for j, c := range word {
            sorted_word[j] = c
        }
        sort.Slice(sorted_word, func(i, j int) bool {
            return sorted_word[i] < sorted_word[j]
        })
        sorted_words[i] = string(sorted_word)
    }

    return strings.Join(sorted_words, " ")
}