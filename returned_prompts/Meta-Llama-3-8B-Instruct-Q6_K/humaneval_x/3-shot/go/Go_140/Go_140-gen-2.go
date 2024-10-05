    var result string
    for _, c := range text {
        if c == ' ' {
            if len(result) > 0 && result[len(result)-1] == ' ' {
                result += "-"
            } else {
                result += "_"
            }
        } else {
            result += string(c)
        }
    }
    return result
}