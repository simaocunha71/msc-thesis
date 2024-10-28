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
    encoded := []rune{}
    for _, c := range message {
        if v, ok := vowels[c]; ok {
            encoded = append(encoded, v)
        } else {
            encoded = append(encoded, c)
        }
    }
    return strings.ToUpper(string(encoded))
}



