    var words = strings.Fields(s)
    var vowels = map[rune]bool{
        'a': true,
        'e': true,
        'i': true,
        'o': true,
        'u': true,
        'A': true,
        'E': true,
        'I': true,
        'O': true,
        'U': true,
    }
    var result = make([]string, 0)

    for _, word := range words {
        var consonants = 0
        for _, letter := range word {
            if !vowels[letter] {
                consonants++
            }
        }
        if consonants == n {
            result = append(result, word)
        }
    }
    return result
}



