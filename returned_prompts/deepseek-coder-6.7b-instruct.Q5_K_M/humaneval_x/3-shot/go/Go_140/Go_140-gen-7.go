    result := ""
    lastWasSpace := false
    for _, c := range text {
        if c == ' ' {
            if lastWasSpace {
                result += "-"
            } else {
                result += "_"
            }
            lastWasSpace = true
        } else {
            result += string(c)
            lastWasSpace = false
        }
    }
    return result
}



