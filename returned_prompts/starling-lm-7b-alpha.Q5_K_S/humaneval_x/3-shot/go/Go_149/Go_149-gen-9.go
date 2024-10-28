    result := make([]string, 0)
    for _, c := range lst {
        if len(c) % 2 == 0 {
            result = append(result, c)
        }
    }
    sort.Slice(result[:], func(i, j int) bool {
        return len(result[i]) < len(result[j])
    })
    return result
}



