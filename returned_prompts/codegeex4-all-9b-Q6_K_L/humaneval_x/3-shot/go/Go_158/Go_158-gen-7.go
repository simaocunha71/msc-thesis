    var max_unique int
    var max_string string

    for _, word := range words {
        unique_chars := make(map[rune]bool)
        for _, c := range word {
            unique_chars[c] = true
        }
        if len(unique_chars) > max_unique {
            max_unique = len(unique_chars)
            max_string = word
        } else if len(unique_chars) == max_unique {
            if word < max_string {
                max_string = word
            }
        }
    }
    return max_string
}



