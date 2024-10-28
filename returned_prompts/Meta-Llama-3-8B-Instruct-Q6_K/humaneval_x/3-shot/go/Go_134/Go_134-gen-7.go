    if len(txt) == 0 {
        return false
    }
    last_char := txt[len(txt)-1]
    if !strings.IsPrint(last_char) {
        return false
    }
    return !strings.Contains(txt[:len(txt)-1], string(last_char))
}