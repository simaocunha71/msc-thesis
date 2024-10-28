    max_word := ""
    max_unique_chars := 0

    for _, word := range words {
        unique_chars := len([]rune(unique(word)))
        if unique_chars > max_unique_chars {
            max_unique_chars = unique_chars
            max_word = word
        }else if unique_chars == max_unique_chars {
            if word < max_word {
                max_word = word
            }
        }
    }
    return max_word
}

func unique(s string) string {
    b := make([]rune, 0)
    for i := 0; i < len(s); i++ {
        if !contains(b, s[i]) {
            b = append(b, s[i])
        }
    }
    return string(b)
}

func contains(b []rune, c rune) bool {
    for _, v := range b {
        if v == c {
            return true
        }
    }
    return false
}