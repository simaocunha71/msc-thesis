    if len(strings) == 0 {
        return nil
    }
    longest := ""
    for _, s := range strings {
        if len(s) > len(longest) {
            longest = s
        }
    }
    return longest
}



