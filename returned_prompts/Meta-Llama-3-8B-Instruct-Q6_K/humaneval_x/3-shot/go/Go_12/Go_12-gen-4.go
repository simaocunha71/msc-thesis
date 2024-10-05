    if len(strings) == 0 {
        return nil
    }
    max_length := 0
    longest_string := strings[0]
    for _, s := range strings {
        if len(s) > max_length {
            max_length = len(s)
            longest_string = s
        }
    }
    return longest_string
}