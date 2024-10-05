    words := strings.Fields(s)
    result := make([]string, 0)

    for _, word := range words {
        if len(word) == n && !strings.ContainsAny(word, "aeiou"){
            result = append(result, word)
        }
    }
    return result
}



