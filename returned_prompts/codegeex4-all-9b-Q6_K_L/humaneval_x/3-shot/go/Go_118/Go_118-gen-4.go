    vowels := "aeiou"
    last := len(word) - 1
    for i := last - 1; i > 0; i-- {
        if bytes.ContainsRune([]byte(vowels), rune(word[i])) {
            return string(word[i])
        }
    }
    return ""
}

