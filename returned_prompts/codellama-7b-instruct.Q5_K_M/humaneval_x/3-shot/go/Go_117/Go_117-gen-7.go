    words := strings.Fields(s)
    var result []string

    for _, word := range words{
        if len(word)==n{
            result = append(result, word)
        }
    }
    return result
}



