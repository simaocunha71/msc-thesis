    last_char := strings.TrimSpace(txt)[len(txt)-1]
    if strings.ContainsAny(last_char, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") &&
        !strings.ContainsAny(txt[len(txt)-2:], "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") {
        return true
    } else {
        return false
    }
}



