    vowels := []rune{'a', 'e', 'i', 'o', 'u'}
    result := make([]rune, 0)
    for _, c := range message {
        if (c >= 'a' && c <= 'z') {
            if (c >= 't' && c <= 'z') && !contains(vowels, c) {
                result = append(result, c)
            } else if (c >= 'a' && c <= 'm') && contains(vowels, c) {
                result = append(result, vowels[((vowels[:len(vowels)])[((vowels[:len(vowels)])[strings.Index(vowels, string(c))+1]+vowels[len(vowels)-1])%len(vowels)]+vowels[len(vowels)-1])%len(vowels)]+vowels[len(vowels)-1])
            } else {
                result = append(result, vowels[((vowels[:len(vowels)])[((vowels[:len(vowels)])[strings.Index(vowels, string(c))+1]+vowels[len(vowels)-1])%len(vowels)]+vowels[len(vowels)-1])%len(vowels)]+vowels[len(vowels)-1])
            }
        } else {
            result = append(result, c)
        }
    }
    return string(result)
}



