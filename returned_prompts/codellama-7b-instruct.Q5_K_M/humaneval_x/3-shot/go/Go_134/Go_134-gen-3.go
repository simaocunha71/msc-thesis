    if len(txt) == 0 {
        return false
    }
    if strings.HasSuffix(txt, " ") {
        return false
    }
    if strings.HasSuffix(txt, "  ") {
        return false
    }
    if strings.HasSuffix(txt, "\n") {
        return false
    }
    if strings.HasSuffix(txt, "\r") {
        return false
    }
    if strings.HasSuffix(txt, "\t") {
        return false
    }
    last_char := string(txt[len(txt)-1])
    return strings.ContainsAny(last_char, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
}



