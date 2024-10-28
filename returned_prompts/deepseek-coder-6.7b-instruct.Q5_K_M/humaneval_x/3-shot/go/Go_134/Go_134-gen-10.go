    if len(txt) == 0 || !strings.Contains(txt, " ") {
        return false
    }
    lastChar := txt[len(txt)-1]
    return (lastChar >= 'a' && lastChar <= 'z') || (lastChar >= 'A' && lastChar <= 'Z')
}



