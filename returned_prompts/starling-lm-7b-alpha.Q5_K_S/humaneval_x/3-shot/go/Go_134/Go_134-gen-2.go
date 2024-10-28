    if len(txt) == 0 {
        return false
    }
    lastChar := txt[len(txt)-1]
    return (lastChar >= 'a' && lastChar <= 'z') || (lastChar >= 'A' && lastChar <= 'Z') && !strings.Contains(txt[:len(txt)-1], " ")
}



