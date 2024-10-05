    sort.Slice(lst, func(i, j int) bool {
        return len(lst[i]) < len(lst[j])
    })

    result := make([]string, 0)
    for _, s := range lst {
        if len(s)%2 == 0 {
            result = append(result, s)
        }
    }
    return result
}



