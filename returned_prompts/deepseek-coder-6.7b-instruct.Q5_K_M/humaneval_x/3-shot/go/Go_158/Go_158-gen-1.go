    sort.Strings(words)
    max := 0
    result := ""

    for _, word := range words {
        unique := make(map[rune]bool)
        for _, letter := range word {
            unique[letter] = true
        }
        if len(unique) > max {
            max = len(unique)
            result = word
        }
    }
    return result
}



