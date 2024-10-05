    result := make([]string, 0)

    for _, word := range lst {
        if len(word) % 2 == 0 {
            result = append(result, word)
        }
    }

    sort.Slice(result, func(i, j int) bool {
        return len(result[i]) < len(result[j])
    })
    return result
}



