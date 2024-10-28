    result := make([]string, 0)
    words := strings.Fields(s)

    for _, word := range words {
        var count int = 0
        for _, c := range word {
            if c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u' {
                count += 1
            }
        }
        if count == n {
            result = append(result, word)
        }
    }
    return result
}