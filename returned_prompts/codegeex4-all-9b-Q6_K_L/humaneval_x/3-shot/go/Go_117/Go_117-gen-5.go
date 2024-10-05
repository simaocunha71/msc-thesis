    result := make([]string, 0)
    split := strings.Fields(s)
    for _, word := range split {
        if len(bytes.TrimSpace(word)) == n {
            result = append(result, word)
        }
    }
    return result
}

