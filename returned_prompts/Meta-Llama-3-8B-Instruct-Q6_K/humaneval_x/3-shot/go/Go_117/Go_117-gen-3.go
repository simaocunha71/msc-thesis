    words := strings.Fields(s)
    result := make([]string, 0)
    for _, word := range words {
        consonants := 0
        for _, c := range word {
            if !strings.Contains("aeiouAEIOU", string(c)) {
                consonants++
            }
        }
        if consonants == n {
            result = append(result, word)
        }
    }
    return result
}  // O(n*m) where n is the number of words and m is the length of the longest word.