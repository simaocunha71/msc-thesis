    sort.Strings(words)

    max_chars, max_word := 0, ""
    for _, word := range words {
        chars := make(map[rune]bool)
        for _, char := range word {
            chars[char] = true
        }
        if len(chars) > max_chars {
            max_chars = len(chars)
            max_word = word
        }
    }

    return max_word
}



