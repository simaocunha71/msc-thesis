    if len(txt) == 0 {
        return false
    }
    lastChar := txt[len(txt) - 1]
    return strings.IsLetter(lastChar) && !strings.Contains(txt, " " + string(lastChar))
}