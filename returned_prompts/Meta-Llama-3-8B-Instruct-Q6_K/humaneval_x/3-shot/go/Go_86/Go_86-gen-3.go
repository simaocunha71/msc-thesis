    words := strings.Split(s, " ")
    result := make([]string, 0)

    for _, word := range words {
        sorted_word := make([]rune, 0)
        for _, c := range word {
            sorted_word = append(sorted_word, rune(c))
        }
        sort.Runes(sorted_word)
        result = append(result, string(sorted_word))
    }
    return strings.Join(result, " ")
}