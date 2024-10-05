    sort.Strings(lst)
    result := make([]string, 0)
    for _, word := range lst {
        if len(word) % 2 == 0 {
            result = append(result, word)
        }
    }
    return result
}



