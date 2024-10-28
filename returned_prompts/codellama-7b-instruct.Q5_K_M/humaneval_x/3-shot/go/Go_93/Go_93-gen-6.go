    runes := []rune(strings.ToUpper(message))

    for i, c := range runes {
        if c >= 'A' && c <= 'Z' {
            if c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U' {
                runes[i] = rune(c + 2)
            }
        }
    }
    return string(runes)
}



