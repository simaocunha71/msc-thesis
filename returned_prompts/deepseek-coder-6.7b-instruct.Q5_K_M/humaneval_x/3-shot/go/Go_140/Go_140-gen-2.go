    result := ""
    consecutiveSpaces := 0
    for _, c := range text {
        if c == ' ' {
            consecutiveSpaces += 1
            if consecutiveSpaces == 2 {
                result += "-"
        }
        } else {
            if consecutiveSpaces > 0 {
                result += "_"
                consecutiveSpaces = 0
            }
            result += string(c)
        }
    }
    return result
}



