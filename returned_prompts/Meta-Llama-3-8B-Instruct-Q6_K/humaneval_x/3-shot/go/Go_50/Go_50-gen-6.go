    runes := []rune(s)
    newRunes := make([]rune, 0)
    for _, ch := range runes {
        newRunes = append(newRunes, (ch-'a'+25)%26+'a')
    }
    return string(newRunes)
} 



