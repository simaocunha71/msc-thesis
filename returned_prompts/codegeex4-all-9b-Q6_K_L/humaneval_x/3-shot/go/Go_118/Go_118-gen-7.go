    vowels := "AEIOUaeiou"
    for i := len(word) - 2; i >= 0; i-- {
        if !bytes.ContainsRune(vowels, rune(word[i])) && bytes.ContainsRune(vowels, rune(word[i+1])) {
            return string(word[i+1])
        }
    }

    return ""
}



