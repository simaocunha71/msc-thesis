    var result string
    var count int
    for _, c := range text {
        if c == ' ' {
            count++
            if count == 1 {
                result += "_"
            } else if count == 2 {
                result += "-"
                count = 0
            }
        } else {
            result += string(c)
            count = 0
        }
    }
    return result
}