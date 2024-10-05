    words := strings.Fields(s)
    result := make([]string, 0)
    for _, word := range words {
        count := 0
        for _, char := range word {
            if !strings.ContainsRune("aeiouAEIOU", char) {
                count++
            }
        }
        if count == n {
            result = append(result, word)
        }
    }
    return result
}