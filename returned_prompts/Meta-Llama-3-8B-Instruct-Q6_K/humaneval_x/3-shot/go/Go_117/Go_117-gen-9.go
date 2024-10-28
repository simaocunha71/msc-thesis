    words := strings.Fields(s)
    result := make([]string, 0)
    for _, word := range words {
        consonant_count := 0
        for _, c := range word {
            if c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'y' || c == ' ' {
                continue
            }
            consonant_count += 1
        }
        if consonant_count == n {
            result = append(result, word)
        }
    }
    return result
}