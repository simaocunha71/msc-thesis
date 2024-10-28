    last_char := strings.ToLower(string(txt[len(txt)-1]))
    if last_char == " " {
        return false
    }
    if strings.ContainsAny(last_char,"abcdefghijklmnopqrstuvwxyz") {
        return true
    }
    return false
}



