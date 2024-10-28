    var result string
    for _, c := range s {
        if c >= 'A' && c <= 'Z' {
            result = string(c + 32) + result
        } else if c >= 'a' && c <= 'z' {
            result = string(c - 32) + result
        } else {
            result = string(c) + result
        }
    }
    return result
}



