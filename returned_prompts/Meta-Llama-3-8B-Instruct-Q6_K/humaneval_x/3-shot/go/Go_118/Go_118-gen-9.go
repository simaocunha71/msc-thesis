    var result string
    for i := len(word) - 1; i >= 0; i-- {
        c := word[i]
        if c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U' {
            if i+1 < len(word) && !isConsonant(word[i+1]) {
                return string(c)
            }
            return string(c)
        }
    }
    return result
}

func isConsonant(c byte) bool {
    return c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u' && c != 'A' && c != 'E' && c != 'I' && c != 'O' && c != 'U'
}