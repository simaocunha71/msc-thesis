    words := strings.Split(s, " ")
    for i := range words {
        runes := []rune(words[i])
        sort.Slice(runes, func(i, j int) bool {
            return runes[i] < runes[j]
        })
        words[i] = string(runes)
    }
    return strings.Join(words, " ")

}

