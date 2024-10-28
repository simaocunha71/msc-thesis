    words := strings.Split(s, " ")
    for i, word := range words {
        var sortedWord []rune
        for _, c := range word {
            sortedWord = append(sortedWord, c)
        }
        sort.Slice(sortedWord, func(i, j int) bool {
            return sortedWord[i] < sortedWord[j]
        })
        words[i] = string(sortedWord)
    }
    return strings.Join(words, " ")
}

