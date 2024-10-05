    max_word := words[0]
    max_len := 0
    for _, word := range words {
        word_len := len(word)
        if word_len > max_len {
            max_len = word_len
            max_word = word
        }
    }
    return max_word
}



