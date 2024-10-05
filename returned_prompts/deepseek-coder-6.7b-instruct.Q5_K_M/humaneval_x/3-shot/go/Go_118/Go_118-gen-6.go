    vowels := []rune{'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    word_r := []rune(word)
    for i := len(word_r) - 2; i > 0; i-- {
        if bytes.ContainsRune([]rune(vowels), word_r[i]) &&
            !bytes.ContainsRune([]rune(vowels), word_r[i+1]) &&
            !bytes.ContainsRune([]rune(vowels), word_r[i-1]) {
            return string(word_r[i])
        }
    }
    return ""
}



