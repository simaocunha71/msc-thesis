    var max_word string
    var max_unique int

    for _, word := range words {
        unique_chars := make(map[rune]bool)
        for _, char := range word {
            unique_chars[char] = true
        }
        if len(unique_chars) > max_unique {
            max_unique = len(unique_chars)
            max_word = word
        }
    }

    sort.Strings(words)
    for _, word := range words {
        unique_chars := make(map[rune]bool)
        for _, char := range word {
            unique_chars[char] = true
        }
        if len(unique_chars) == max_unique {
            return word
        }
    }
    return max_word
}