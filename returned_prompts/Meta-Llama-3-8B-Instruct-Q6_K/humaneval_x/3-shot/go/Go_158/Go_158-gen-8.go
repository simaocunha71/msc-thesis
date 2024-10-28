    var max_word string
    var max_unique int
    for _, word := range words {
        unique_chars := make(map[rune]bool)
        for _, c := range word {
            unique_chars[c] = true
        }
        if len(unique_chars) > max_unique {
            max_unique = len(unique_chars)
            max_word = word
        }
    }
    if max_word == "" {
        return ""
    }
    for _, word := range words {
        if word == max_word {
            return word
        }
    }
    return ""
} 



