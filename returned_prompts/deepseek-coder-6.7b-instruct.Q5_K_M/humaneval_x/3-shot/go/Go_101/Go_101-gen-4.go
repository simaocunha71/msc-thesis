    return strings.FieldsFunc(s, func(c rune) bool {
        return c == ',' || c == ' '
    })
}



