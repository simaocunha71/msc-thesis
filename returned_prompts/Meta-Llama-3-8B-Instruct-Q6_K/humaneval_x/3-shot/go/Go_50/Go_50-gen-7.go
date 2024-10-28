    runes := []rune(s)
    newRunes := make([]rune, 0)
    for _, ch := range runes {
        newRunes = append(newRunes, (ch-'a'+26)%26+'a')
    }
    return string(newRunes)
} 





