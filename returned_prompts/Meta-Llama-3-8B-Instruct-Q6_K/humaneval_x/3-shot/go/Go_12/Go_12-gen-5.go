    if len(strings) == 0 {
        return nil
    }
    longest_str := strings[0]
    for _, str := range strings {
        if len(str) > len(longest_str) {
            longest_str = str
        }
    }
    return longest_str
}  // or return longest_str[0] if you want to return the first one in case of multiple strings of the same length.