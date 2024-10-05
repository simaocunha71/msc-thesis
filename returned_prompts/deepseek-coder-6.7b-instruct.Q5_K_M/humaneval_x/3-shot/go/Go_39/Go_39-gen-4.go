    var result string
    for _, c := range s {
        if unicode.IsLetter(c) {
            c += rune(shift)
            if unicode.IsUpper(c) && c > 'Z' || unicode.IsLower(c) && c > 'z' {
                c -= 26
            }
        }
        result += string(c)
    }
    return result
}



