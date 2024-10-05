    vowels := map[rune]rune{
        'a': 'c',
        'e': 'g',
        'i': 'k',
        'o': 'q',
        'u': 'w',
        'A': 'C',
        'E': 'G',
        'I': 'K',
        'O': 'Q',
        'U': 'W',
    }
    result := make([]rune, len(message))
    for i, c := range message {
        if v, ok := vowels[c]; ok {
            result[i] = v
        } else {
            if c >= 'a' && c <= 'z' {
                result[i] = rune(c - 32)
            } else if c >= 'A' && c <= 'Z' {
                result[i] = rune(c + 32)
            } else {
                result[i] = c
            }
        }
    }
    return string(result)
}



