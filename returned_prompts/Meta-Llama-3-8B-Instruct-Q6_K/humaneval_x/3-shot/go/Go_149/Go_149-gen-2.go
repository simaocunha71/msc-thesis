    var result []string
    for _, word := range lst {
        if len(word)%2 == 0 {
            result = append(result, word)
        }
    }
    sort.Slice(result, func(i, j int) bool {
        if len(result[i]) == len(result[j]) {
            return result[i] < result[j]
        }
        return len(result[i]) < len(result[j])
    })
    return result
}