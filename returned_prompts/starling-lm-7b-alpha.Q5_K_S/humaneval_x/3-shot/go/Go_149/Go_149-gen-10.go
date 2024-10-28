    result := make([]string, 0)
    for _, c := range lst {
        if len(c)%2==0 {
            result = append(result, c)
        }
    }
    sort.Slice(result, func(i int, j int) bool {
        return len(result[i]) < len(result[j]) || (len(result[i]) == len(result[j]) && result[i] < result[j])
    })
    return result
}



