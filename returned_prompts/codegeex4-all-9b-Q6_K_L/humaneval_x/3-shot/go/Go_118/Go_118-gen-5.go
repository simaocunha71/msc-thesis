    vowels := "AEIOU"
    result := ""
    for i := len(word)-1; i > 0; i-- {
        if vowels[bytes.IndexByte(vowels, word[i])] == word[i] && !isConsonant(word[i-1]) && !isConsonant(word[i+1]) {
            result = string(word[i])
            break
        }
    }
    return result
}

func isConsonant(c byte) bool {
    return bytes.IndexByte("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ", c) != -1
}

