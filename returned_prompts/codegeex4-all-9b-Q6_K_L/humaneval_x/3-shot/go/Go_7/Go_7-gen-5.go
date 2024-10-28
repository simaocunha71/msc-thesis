    result := make([]string, 0)
    for _, word := range stringList {
        if strings.Contains(word, substring) {
            result = append(result, word)
        }
    }
    return result
}



