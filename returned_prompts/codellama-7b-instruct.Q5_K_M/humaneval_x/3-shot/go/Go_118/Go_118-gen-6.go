    word_runes := []rune(word)

    if len(word_runes) == 0 {
        return ""
    }

    for i := len(word_runes) - 1; i >= 0; i-- {
        if isVowel(word_runes[i]) {
            if i+1 < len(word_runes) && isConsonant(word_runes[i+1]) {
                return string(word_runes[i])
            }
        }
    }
    return ""
}

func isConsonant(r rune) bool {
    return r != 'a' && r != 'e' && r != 'i' && r != 'o' && r != 'u' && r != 'A' && r != 'E' && r != 'I' && r != 'O' && r != 'U'
}

func isVowel(r rune) bool {
    return r == 'a' || r == 'e' || r == 'i' || r == 'o' || r == 'u' || r == 'A' || r == 'E' || r == 'I' || r == 'O' || r == 'U'
}







