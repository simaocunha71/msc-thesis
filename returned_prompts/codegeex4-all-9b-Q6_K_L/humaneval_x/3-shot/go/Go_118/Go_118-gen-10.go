    vowels := "AEIOUaeiou"
    var result string

    for i := len(word) - 1; i > 0; i-- {
        if !bytes.ContainsRune(vowels, rune(word[i])) {
            if bytes.ContainsRune(vowels, rune(word[i-1])) {
                result = word[i-1 : i]
                break
            }
        }
    }

    return result
}



