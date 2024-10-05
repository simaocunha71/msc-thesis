    sort.Slice(words, func(i, j int) bool {
        return len(words[i]) > len(words[j])
    })
    unique_chars := make(map[rune]bool)
    max_unique_chars := 0
    max_word := ""
    for _, word := range words {
        unique_chars_word := 0
        for _, char := range word {
            _, found := unique_chars[char]
            if !found {
                unique_chars_word += 1
                unique_chars[char] = true
            }
        }
        if unique_chars_word > max_unique_chars {
            max_unique_chars = unique_chars_word
            max_word = word
        }
    }
    return max_word
}



