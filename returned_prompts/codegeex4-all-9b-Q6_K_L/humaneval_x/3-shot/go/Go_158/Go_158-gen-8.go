    var max_word string
    max_len := 0

    for _, word := range words {
        if len(word) > max_len {
            max_len = len(word)
            max_word = word
        } else if len(word) == max_len {
            if word < max_word {
                max_word = word
            }
        }
    }
    return max_word
}



