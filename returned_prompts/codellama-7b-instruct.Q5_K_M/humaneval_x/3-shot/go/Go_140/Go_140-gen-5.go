    result := ""
    for i := 0; i < len(text); i++ {
        if text[i] == ' ' {
            if i + 1 < len(text) && text[i + 1] == ' ' {
                result += "-"
                i += 1
            } else {
                result += "_"
            }
        } else {
            result += text[i]
        }
    }
    return result
}



