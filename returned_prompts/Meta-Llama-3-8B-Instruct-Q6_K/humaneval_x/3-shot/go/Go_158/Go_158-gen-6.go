    max_len := 0
    max_str := ""

    for _, word := range words {
        unique_chars := make(map[rune]bool)
        for _, char := range word {
            unique_chars[char] = true
        }
        if len(unique_chars) > max_len {
            max_len = len(unique_chars)
            max_str = word
        }
    }

    if max_len == 0 {
        return ""
    }
    return max_str
} 



