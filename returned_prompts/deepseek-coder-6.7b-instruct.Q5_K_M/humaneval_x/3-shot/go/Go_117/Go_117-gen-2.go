    var result []string
    words := strings.Fields(s)
    for _, word := range words {
        count := 0
        for _, c := range word {
            if strings.ContainsRune("aeiouAEIOU", c) {
                continue
            }
            count++
        }
        if count == n {
            result = append(result, word)
        }
    }
    return result
}



