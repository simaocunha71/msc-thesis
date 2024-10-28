    // Filter list to have only strings with even length
    var result []string
    for _, word := range lst {
        if len(word)%2 == 0 {
            result = append(result, word)
        }
    }

    // Sort list by length and alphabetical order
    sort.Slice(result, func(i, j int) bool {
        if len(result[i]) != len(result[j]) {
            return len(result[i]) < len(result[j])
        }
        return result[i] < result[j]
    })
    return result
}



