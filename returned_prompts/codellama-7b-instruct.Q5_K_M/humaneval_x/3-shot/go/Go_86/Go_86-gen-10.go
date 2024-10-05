    words := strings.Split(s," ")
    sorted_words := make([]string, 0)
    for _, word := range words {
        sorted_words = append(sorted_words, SortWord(word))
    }
    return strings.Join(sorted_words," ")
}

func SortWord(word string) string {
    var sorted_word []rune
    for _, r := range word{
        sorted_word = append(sorted_word,r)
    }
    sort.SliceStable(sorted_word, func(i, j int) bool {
        return sorted_word[i] < sorted_word[j]
    })
    return string(sorted_word)
}



