    sort.Strings(lst)
    result := make([]string, 0)
    current_length := 0
    for _, s := range lst {
        if len(s) != current_length {
            if len(result) != 0 {
                result = append(result, s)
            }
            current_length = len(s)
        }
    }
    return result
}



