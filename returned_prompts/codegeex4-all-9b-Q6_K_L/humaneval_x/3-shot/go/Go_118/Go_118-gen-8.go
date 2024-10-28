    vowels := []rune{'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    for i := len(word) - 1; i > 0; i-- {
        if bytes.IndexRune(vowels, rune(word[i])) > -1 {
            if bytes.IndexRune(vowels, rune(word[i-1])) > -1 || bytes.IndexRune(vowels, rune(word[i+1])) > -1 {
                continue
            }
            return string(word[i])
        }
    }

    return ""
}

