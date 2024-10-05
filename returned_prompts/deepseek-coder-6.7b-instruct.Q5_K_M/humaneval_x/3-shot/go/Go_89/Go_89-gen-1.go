    var result string
    for _, c := range s {
        if c >= 'a' && c <= 'z' {
            result += string((c-'a'+2*2)%26 + 'a')
        } else if c >= 'A' && c <= 'Z' {
            result += string((c-'A'+2*2)%26 + 'A')
        } else {
            result += string(c)
        }
    }
    return result
}



