    var vowels = "aeiouAEIOU"
    var buffer bytes.Buffer

    for i := len(word) - 2; i > 0; i-- {
        if strings.ContainsRune(vowels, rune(word[i])) &&
            !strings.ContainsRune(vowels, rune(word[i+1])) &&
            !strings.ContainsRune(vowels, rune(word[i-1])) {
            buffer.WriteByte(word[i])
            break
        }
    }

    return buffer.String()
}



