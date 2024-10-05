    if len(txt) == 0 || !strings.ContainsRune("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", txt[len(txt)-1]) {
        return false
    }
    if strings.ContainsRune(" ", txt[len(txt)-2:]) {
        return true
    }
    return false
}



