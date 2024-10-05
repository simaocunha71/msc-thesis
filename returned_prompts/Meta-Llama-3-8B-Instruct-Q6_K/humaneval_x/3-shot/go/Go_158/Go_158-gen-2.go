    var max_word string
    var max_length int

    for _, word := range words {
        unique_chars := make(map[rune]bool)
        for _, char := range word {
            unique_chars[char] = true
        }
        if len(unique_chars) > max_length {
            max_length = len(unique_chars)
            max_word = word
        } else if len(unique_chars) == max_length {
            if word < max_word {
                max_word = word
            }
        }
    }
    return max_word
}