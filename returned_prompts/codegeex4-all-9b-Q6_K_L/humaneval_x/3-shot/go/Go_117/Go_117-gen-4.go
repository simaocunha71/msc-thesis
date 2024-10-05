    result := make([]string, 0)

    consonants := map[rune]bool{
        'b': true,
        'c': true,
        'd': true,
        'f': true,
        'g': true,
        'h': true,
        'j': true,
        'k': true,
        'l': true,
        'm': true,
        'n': true,
        'p': true,
        'q': true,
        'r': true,
        's': true,
        't': true,
        'v': true,
        'w': true,
        'x': true,
        'y': true,
        'z': true,
    }

    words := strings.Fields(s)
    for _, word := range words {
        word_consonants := 0
        for _, letter := range word {
            if consonants[letter] {
                word_consonants++
            }
        }
        if word_consonants == n {
            result = append(result, word)
        }
    }
    return result
}

