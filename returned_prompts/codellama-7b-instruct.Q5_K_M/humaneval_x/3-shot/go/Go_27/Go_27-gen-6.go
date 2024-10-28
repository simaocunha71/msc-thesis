    result := ""
    for _, r := range str {
        if r >= 'a' && r <= 'z' {
            result += string(r - 32)
        } else if r >= 'A' && r <= 'Z' {
            result += string(r + 32)
        } else {
            result += string(r)
        }
    }
    return result
}



