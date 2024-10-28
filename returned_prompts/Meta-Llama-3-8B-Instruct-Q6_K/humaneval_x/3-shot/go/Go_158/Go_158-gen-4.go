    var max_word string
    max_chars := 0
    for _, word := range words {
        chars := make(map[rune]bool)
        for _, c := range word {
            chars[c] = true
        }
        if len(chars) > max_chars {
            max_chars = len(chars)
            max_word = word
        } else if len(chars) == max_chars {
            if word < max_word {
                max_word = word
            }
        }
    }
    return max_word
}