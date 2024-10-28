    if len(strings) == 0 {
        return nil
    }

    var longest string
    var maxLength int

    for _, s := range strings {
        if len(s) > maxLength {
            maxLength = len(s)
            longest = s
        }
    }

    return longest
}