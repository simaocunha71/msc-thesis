    var result string

    for _, c := range s {
        if c >= 'a' && c <= 'z' {
            result += string(c - 32)
        }else if c >= 'A' && c <= 'Z' {
            result += string(c + 32)
        }else {
            result += string(c)
        }
    }
    return result
}



