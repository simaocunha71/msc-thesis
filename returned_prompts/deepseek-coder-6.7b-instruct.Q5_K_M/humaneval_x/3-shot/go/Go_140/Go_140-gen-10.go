    result := ""
    last_was_space := false
    for _, c := range text {
        if c == ' ' {
            if last_was_space {
                result += "-"
            } else {
                result += "_"
            }
            last_was_space = true
        } else {
            result += string(c)
            last_was_space = false
        }
    }
    return result
}



