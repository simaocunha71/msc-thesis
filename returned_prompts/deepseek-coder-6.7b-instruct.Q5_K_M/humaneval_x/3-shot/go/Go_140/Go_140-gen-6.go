    prevWasSpace := false
    result := make([]rune, 0, len(text))
    for _, ch := range text {
        if ch == ' ' {
            if prevWasSpace {
                result = append(result, '-')
            } else {
                result = append(result, '_')
            }
            prevWasSpace = true
        } else {
            result = append(result, ch)
            prevWasSpace = false
        }
    }
    return string(result)
}



