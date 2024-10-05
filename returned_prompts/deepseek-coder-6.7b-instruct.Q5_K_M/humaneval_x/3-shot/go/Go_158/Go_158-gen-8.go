    sort.Strings(words)
    max_unique := 0
    max_word := ""

    for _, word := range words {
        unique := make(map[rune]bool)
        for _, char := range word {
            unique[char] = true
        }
        count := len(unique)
        if count > max_unique {
            max_unique = count
            max_word = word
        }
    }
    return max_word
}



