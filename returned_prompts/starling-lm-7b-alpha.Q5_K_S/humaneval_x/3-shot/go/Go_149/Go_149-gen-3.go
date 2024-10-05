    result := make([]string, 0)
    for _, s := range lst {
        if len(s) % 2 == 0 {
            result = append(result, s)
        }
    }
    sort.Slice(result, func(i, j int) bool {
        return len(result[i]) < len(result[j])
    })
    return result
}



