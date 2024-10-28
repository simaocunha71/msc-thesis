    sort.Strings(words)
    max_count  := 0
    max_word  := ""

    for _, word  := range words {
        unique_chars  := make(map[rune]bool)
        for _, char  := range word {
            unique_chars[char] = true
        }
        count  := len(unique_chars)
        if count > max_count {
            max_count = count
            max_word = word
        }
    }

    return max_word
}



