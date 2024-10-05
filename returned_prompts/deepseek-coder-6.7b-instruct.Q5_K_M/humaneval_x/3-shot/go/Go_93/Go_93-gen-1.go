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

    encoded := []rune(message)

    for i, c := range encoded {
        if _, ok := vowels[c]; ok {
            encoded[i] = vowels[c]
        } else if unicode.IsLower(c) {
            encoded[i] = unicode.ToUpper(c)
        } else if unicode.IsUpper(c) {
            encoded[i] = unicode.ToLower(c)
        }
    }
    return string(encoded)
}



