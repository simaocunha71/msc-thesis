    var result string

    for _, c := range s {
        if 'a' <= c && c <= 'z' {
            result = result + string('a' + (c - 'a' + 2) % 26)
        } else if 'A' <= c && c <= 'Z' {
            result = result + string('A' + (c - 'A' + 2) % 26)
        } else {
            result = result + string(c)
        }
    }
    return result
}



