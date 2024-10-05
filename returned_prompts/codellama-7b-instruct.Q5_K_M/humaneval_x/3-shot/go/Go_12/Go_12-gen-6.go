    var longest_string interface{}
    var longest_length int = 0

    for _, s := range strings {
        if len(s) > longest_length {
            longest_length = len(s)
            longest_string = s
        }
    }
    return longest_string
}



