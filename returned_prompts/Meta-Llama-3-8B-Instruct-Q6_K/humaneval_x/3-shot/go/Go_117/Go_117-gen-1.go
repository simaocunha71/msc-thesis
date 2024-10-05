    var result []string
    words := strings.Fields(s)
    for _, word := range words {
        var consonants int
        for _, r := range word {
            switch {
            case r == 'a' || r == 'e' || r == 'i' || r == 'o' || r == 'u':
                // vowel
            default:
                consonants++
            }
        }
        if consonants == n {
            result = append(result, word)
        }
    }
    return result
}