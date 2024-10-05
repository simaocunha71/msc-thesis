    var vowels = "aeiouAEIOU"
    var buffer bytes.Buffer
    for i := len(word) - 1; i > 0; i-- {
        buffer.WriteByte(word[i])
        if strings.ContainsRune(vowels, rune(word[i])) && !strings.ContainsRune(vowels, rune(word[i-1])) && !strings.ContainsRune(vowels, rune(word[i+1])) {
            return string(word[i])
        }
    }
    return ""
}



