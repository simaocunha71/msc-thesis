    var vowels = "aeiouAEIOU"
    for i := len(word) - 2; i > 0; i-- {
        if strings.ContainsRune(vowels, rune(word[i+1])) && strings.ContainsRune(vowels, rune(word[i-1])) {
            if bytes.ContainsRune([]byte(vowels), rune(word[i])) {
                return string(word[i])
            }
        }
    }
    return ""
}



