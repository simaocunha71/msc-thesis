    if len(strings) == 0 {
        return nil
    }

    longest_string := strings[0]
    longest_length := len(longest_string)

    for _, s := range strings {
        if len(s) > longest_length {
            longest_length = len(s)
            longest_string = s
        }
    }
    return longest_string
}



