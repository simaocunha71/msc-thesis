    result := ""
    for _, c := range s{
        if c >= 'a' && c <= 'z' {
            result += string('a' + ((c - 'a' + 2*2) % 26))
        }else if c >= 'A' && c <= 'Z' {
            result += string('A' + ((c - 'A' + 2*2) % 26))
        }else {
            result += string(c)
        }
    }
    return result
}



