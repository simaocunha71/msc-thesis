    words := strings.Fields(s)
    result := make([]string, 0)
    for _, word := range words {
        count := 0
        for _, c := range word {
            if !strings.Contains("aeiouAEIOU", string(c)) {
                count++
            }
        }
        if count == n {
            result = append(result, word)
        }
    }
    return result
}