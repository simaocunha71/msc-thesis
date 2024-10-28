    words := strings.Split(s, " ")
    result := make([]string, 0)

    for _, word := range words {
        consonants := 0
        for _, c := range word {
            if c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u' && c != ' ' {
                consonants++
            }
        }
        if consonants == n {
            result = append(result, word)
        }
    }
    return result
}