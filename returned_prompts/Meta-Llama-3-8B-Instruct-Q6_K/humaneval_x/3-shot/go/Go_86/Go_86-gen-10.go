    words := strings.Split(s, " ")
    for i, word := range words {
        sortedWord := sort.StringSlice(word)
        sortedWord.Sort()
        words[i] = strings.Join(sortedWord, "")
    }
    return strings.Join(words, " ")
}