    result := make([]rune, len(s))
    for i, r := range s {
        result[i] = r
    }
    sort.Slice(result[:], func(i, j int) bool {
        return int(result[i]) < int(result[j])
    })
    return string(result)
}



