    if len(strings) == 0 {
        return nil
    }
    longest_string := strings[0]
    for _, string := range strings {
        if len(string) > len(longest_string) {
            longest_string = string
        }
    }
    return longest_string
}



