    odd_length_strings := make([]string, 0)
    for _, s := range lst {
        if len(s)%2 == 0 {
            odd_length_strings = append(odd_length_strings, s)
        }
    }
    sort.Strings(odd_length_strings)
    return odd_length_strings
}



