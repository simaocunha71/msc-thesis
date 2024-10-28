    swap := func(r rune) rune {
        if 'a' <= r && r <= 'z' {
            return r - 'a' + 'A'
        } else if 'A' <= r && r <= 'Z' {
            return r - 'A' + 'a'
        } else {
            return r
        }
    }
    return strings.Map(swap, str)
}



