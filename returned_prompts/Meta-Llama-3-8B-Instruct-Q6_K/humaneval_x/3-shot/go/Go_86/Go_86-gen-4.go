    words := strings.Split(s, " ")
    result := make([]string, len(words))
    for i, word := range words {
        runes := []rune(word)
        sort.Runes(runes)
        result[i] = string(runes)
    }
    return strings.Join(result, " ")
}