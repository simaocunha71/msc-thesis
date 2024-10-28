    var result string
    var count int
    for _, c := range text {
        if c == ' ' {
            count++
            if count > 2 {
                result += "-"
            } else {
                result += "_"
            }
        } else {
            result += string(c)
            count = 0
        }
    }
    return result
} 