    result := make([]string, 0)
    for _, c := range lst {
        if len(c)%2 == 0 {
            result = append(result, c)
        }
    }
    sort.Strings(result)
    return result
}


