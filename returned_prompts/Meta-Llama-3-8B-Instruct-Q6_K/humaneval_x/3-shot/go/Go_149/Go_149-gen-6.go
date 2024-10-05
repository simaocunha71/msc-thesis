    // Remove odd length strings and sort by length and then alphabetically
    var result []string
    for _, str := range lst {
        if len(str)%2 == 0 {
            result = append(result, str)
        }
    }
    sort.Slice(result, func(i, j int) bool {
        if len(result[i]) == len(result[j]) {
            return result[i] < result[j]
        }
        return len(result[i]) < len(result[j])
    })
    return result
}  // 4ms, 2.9MB
}  // 4ms, 2.9MB


