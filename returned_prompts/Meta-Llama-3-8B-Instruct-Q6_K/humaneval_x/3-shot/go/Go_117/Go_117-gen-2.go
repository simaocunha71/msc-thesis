    var result []string
    words := strings.Split(s, " ")
    for _, word := range words {
        var consonants int
        for _, char := range word {
            if !strings.Contains("aeiouAEIOU", string(char)) {
                consonants++
            }
        }
        if consonants == n {
            result = append(result, word)
        }
    }
    return result
}