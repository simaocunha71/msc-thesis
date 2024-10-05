    var vowels = []rune{'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    for i := len(word) - 2; i > 0; i-- {
        if bytes.ContainsRune(vowels, rune(word[i+1])) && bytes.ContainsRune(vowels, rune(word[i-1])) {
            if bytes.ContainsRune(vowels, rune(word[i])) {
                continue
            } else {
                return string(word[i])
            }
        }
    }
    return ""
}



