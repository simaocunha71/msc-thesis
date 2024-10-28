    words := strings.Fields(s)
    result := make([]string, 0)
    for _, word := range words {
        consonants := 0
        for _, r := range word {
            if r != 'a' && r != 'e' && r != 'i' && r != 'o' && r != 'u' && r != ' ' {
                consonants++
            }
        }
        if consonants == n {
            result = append(result, word)
        }
    }
    return result
}



