    result := make([]string, 0)
    for _, v := range lst {
        if len(v) % 2 == 0 {
            result = append(result, v)
        }
    }
    sort.Strings(result)
    return result
}



