    if len(txt) == 0 {
        return false
    }
    lastChar := txt[len(txt)-1]
    if !strings.ContainsAny(string(lastChar), "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") {
        return false
    }
    if strings.Contains(txt, string(lastChar)) {
        return false
    }
    return true
}
