    words := strings.Split(s, " ")
    result := make([]string, len(words))
    for i, word := range words {
        bytes := []byte(word)
        sort.Slice(bytes, func(i, j int) bool {
            return bytes[i] < bytes[j]
        })
        result[i] = string(bytes)
    }
    return strings.Join(result, " ")
}