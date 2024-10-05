    result := make([]string, 0)
    for _, word := range strings{
        if strings.HasPrefix(word, prefix){
            result = append(result, word)
        }
    }
    return result
}



