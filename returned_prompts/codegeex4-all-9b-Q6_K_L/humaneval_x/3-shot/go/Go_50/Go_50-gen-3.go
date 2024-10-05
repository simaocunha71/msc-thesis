    runes := []rune(s)
    newRunes := make([]rune, 0)
    for _, ch := range runes {
        newRunes = append(newRunes, alphabet[ch-'a'])
    }
    return string(newRunes)
}

