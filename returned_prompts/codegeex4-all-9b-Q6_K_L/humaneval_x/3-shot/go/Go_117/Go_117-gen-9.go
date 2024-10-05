    result := make([]string, 0)
    words := strings.Split(s, " ")
    for _, word := range words {
        consonant_count := 0
        for _, c := range word {
            if c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u' {
                consonant_count += 1
            }
        }
        if consonant_count == n {
            result = append(result, word)
        }
    }
    return result
}



