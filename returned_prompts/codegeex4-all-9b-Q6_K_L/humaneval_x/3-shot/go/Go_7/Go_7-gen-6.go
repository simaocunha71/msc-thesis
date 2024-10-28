    var result []string
    for _, word := range stringList {
        if strings.Contains(word, substring) {
            result = append(result, word)
        }
    }
    return result
}

