    words := strings.Split(s, " ")
    for i := range words {
        sort.Runes([]rune(words[i]))
    }
    return strings.Join(words, " ")
}