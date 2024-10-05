    sort.Strings(lst)
    result := make([]string, 0)

    for _, s := range lst {
        if len(s)%2 == 0 {
            result = append(result, s)
        }
    }

    return result
}



