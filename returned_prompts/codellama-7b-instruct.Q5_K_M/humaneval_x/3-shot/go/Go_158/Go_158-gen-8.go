    if len(words) == 0 {
        return ""
    }

    var max_count int = 0
    var max_word string = ""

    for _, word := range words {
        if len(word) > max_count {
            max_count = len(word)
            max_word = word
        }
    }

    for _, word := range words {
        if len(word) == max_count && len(word) > len(max_word) {
            max_word = word
        }
    }
    return max_word
}



