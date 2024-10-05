    words := strings.Fields(s)
    for i := range words {
        word := []rune(words[i])
        sort.Slice(word, func(i, j int) bool { return word[i] < word[j] })
        words[i] = string(word)
    }
    return strings.Join(words, " ")
}



