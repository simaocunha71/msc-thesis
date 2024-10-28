    words := strings.Split(s, " ")
    for i := range words {
        runes := []rune(words[i])
        sort.Runes(runes)
        words[i] = string(runes)
    }
    return strings.Join(words, " ")
}