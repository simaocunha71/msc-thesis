    if len(strings) == 0 {
        return nil
    }
    longest := strings[0]
    for _, s := range strings[1:] {
        if len(longest) < len(s) {
            longest = s
        }
    }
    return longest
}



