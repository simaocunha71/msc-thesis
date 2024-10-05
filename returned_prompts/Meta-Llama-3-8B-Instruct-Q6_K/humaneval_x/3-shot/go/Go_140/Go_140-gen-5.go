    var result string
    i := 0
    for _, c := range text {
        if c == ' ' {
            if i > 0 && result[i-1] == ' ' {
                result += "-"
            } else {
                result += "_"
            }
            i = 0
        } else {
            result += string(c)
            i++
        }
    }
    return result
} 





