    if len(words) == 0 {
        return ""
    }

    var max_word string
    var max_length int = 0

    for _, word := range words {
        if len(word) > max_length {
            max_length = len(word)
            max_word = word
        }
    }

    for _, word := range words {
        if len(word) == max_length && len(word) > 0 && word != max_word {
            if word < max_word {
                max_word = word
            }
        }
    }
    return max_word
}



