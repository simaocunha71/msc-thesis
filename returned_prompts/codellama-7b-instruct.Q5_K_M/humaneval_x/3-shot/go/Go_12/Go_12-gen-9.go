    if len(strings) == 0 {
        return nil
    }
    var longest string = strings[0]
    for i := 1; i < len(strings); i++ {
        if len(strings[i]) > len(longest) {
            longest = strings[i]
        }
    }
    return longest
}



