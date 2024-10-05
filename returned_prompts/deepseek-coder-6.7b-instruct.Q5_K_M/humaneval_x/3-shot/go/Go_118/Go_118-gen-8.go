    vowels := "AEIOUaeiou"
    for i := len(word) - 2; i > 0; i-- {
        if !bytes.ContainsRune([]byte(vowels), rune(word[i+1])) && bytes.ContainsRune([]byte(vowels), rune(word[i-1])) {
            return string(word[i])
        }
    }
    return ""
}



