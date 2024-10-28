    if len(txt) == 0 {
        return false
    }
    last_char := txt[len(txt)-1]
    if !strings.IsDigit(last_char) && !strings.Contains(txt[:len(txt)-1], string(last_char)) {
        return strings.IsLetter(last_char)
    }
    return false
}