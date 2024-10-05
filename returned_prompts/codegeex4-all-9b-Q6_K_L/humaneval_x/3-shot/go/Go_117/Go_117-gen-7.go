    result := make([]string, 0)
    vowels := map[rune]bool{
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
    words := strings.Split(s, " ")
    for _, word := range words {
        consonants := 0
        for _, c := range word {
            if _, ok := vowels[c]; !ok {
                consonants += 1
            }
        }
        if consonants == n {
            result = append(result, word)
        }
    }
    return result
}



