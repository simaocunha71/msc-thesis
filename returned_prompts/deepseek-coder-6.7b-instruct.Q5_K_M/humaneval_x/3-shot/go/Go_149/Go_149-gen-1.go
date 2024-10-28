    result := make([]string, 0)
    for _, word := range lst {
        if len(word) % 2 == 0 {
            result = append(result, word)
        }
    }
    sort.Slice(result, func(i, j int) bool {
        if len(result[i]) < len(result[j]) {
            return true
        } else if len(result[i]) > len(result[j]) {
            return false
        } else {
            return result[i] < result[j]
        }
    })
    return result
}



