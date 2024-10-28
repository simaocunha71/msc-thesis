    var max_word_chars int
    var max_word string

    for _, word := range words {
        unique_chars := make(map[rune]bool)
        for _, c := range word {
            unique_chars[c] = true
        }
        unique_chars_len := len(unique_chars)
        if unique_chars_len > max_word_chars {
            max_word = word
            max_word_chars = unique_chars_len
        }else if unique_chars_len == max_word_chars && word < max_word {
            max_word = word
        }
    }
    return max_word
}



