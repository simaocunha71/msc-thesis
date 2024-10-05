    if len(words) == 0 {
        return ""
    }
    var max_length int = len(words[0])
    var max_word string = words[0]
    for _, word := range words {
        if len(word) > max_length {
            max_length = len(word)
            max_word = word
        }
    }
    return max_word
}



