    var max_word string
    var max_chars int

    for _, word := range words {
        chars := make(map[rune]bool)
        for _, c := range word {
            chars[c] = true
        }
        if len(chars) > max_chars {
            max_chars = len(chars)
            max_word = word
        }
    }
    sort.Strings(words)
    for _, word := range words {
        chars := make(map[rune]bool)
        for _, c := range word {
            chars[c] = true
        }
        if len(chars) == max_chars {
            return word
        }
    }
    return max_word
}