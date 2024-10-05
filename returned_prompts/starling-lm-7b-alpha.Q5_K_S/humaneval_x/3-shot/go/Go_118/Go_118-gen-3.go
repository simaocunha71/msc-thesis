    vowels := []rune{'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    for _, c := range word {
        if !bytes.ContainsRune([]rune{'a', 'e', 'i', 'o', 'u'}, c) {
            continue
        }
        if c == word[len(word)-1] {
            continue
        }
        for _, c2 := range word[len(word)-1:] {
            if bytes.ContainsRune(vowels, c2) {
                continue
            }
            if c2 == word[len(word)-1] {
                continue
            }
            return string(c)
        }
    }
    return ""
}




