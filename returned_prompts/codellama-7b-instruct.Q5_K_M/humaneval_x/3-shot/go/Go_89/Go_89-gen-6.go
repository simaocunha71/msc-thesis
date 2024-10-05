    runes := []rune(s)

    var result string

    for _, r := range runes {
        if r >= 'a' && r <= 'z' {
            result += string(rune(r + 2 * 2))
        } else if r >= 'A' && r <= 'Z' {
            result += string(rune(r + 2 * 2 - 32))
        } else {
            result += string(r)
        }
    }

    return result
}



