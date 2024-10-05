    var newString []rune
    for _, c := range s {
        if 'a' <= c && c <= 'z' {
            newString = append(newString,unicode.ToUpper(c))
        } else if 'A' <= c && c <= 'Z' {
            newString = append(newString,unicode.ToLower(c))
        } else {
            newString = append(newString,c)
        }
    }
    return string(newString)
}



