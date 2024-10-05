    var result string
    for _, c := range strings.ToUpper(message) {
        if c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U' {
            result += string(rune(c+2))
        }else if c == ' ' {
            result += string(c)
        }else {
            result += string(rune(c-2))
        }
    }
    return result
}



