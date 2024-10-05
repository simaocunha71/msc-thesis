    if len(txt) == 0 {
        return false
    }
    last_char := txt[len(txt) - 1]
    if !strings.IsSpace(last_char) && (strings.IsLetter(last_char)) {
        return true
    }
    return false
}