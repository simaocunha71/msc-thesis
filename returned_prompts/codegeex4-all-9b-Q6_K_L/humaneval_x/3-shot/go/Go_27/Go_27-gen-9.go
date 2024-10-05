    return strings.Map(func(r rune) rune {
        switch {
        case 'a' <= r && r <= 'z':
            return r - 'a' + 'A'
        case 'A' <= r && r <= 'Z':
            return r - 'A' + 'a'
        default:
            return r
        }
    }, str)
}


