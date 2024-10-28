    var result string
    var prev rune
    for _, c := range text {
        if c == ' ' && prev == ' ' {
            result += "-"
        } else if c == ' ' {
            result += "_"
        } else {
            result += string(c)
        }
        prev = c
    }
    return result
}



