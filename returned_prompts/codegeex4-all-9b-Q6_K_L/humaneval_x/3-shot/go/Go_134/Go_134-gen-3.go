    if len(txt) == 0 {
        return false
    }
    last := txt[len(txt)-1]
    if !strings.ContainsRune("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", last) {
        return false
    }
    if len(txt) == 1 {
        return true
    }
    prev := txt[len(txt)-2]
    return !strings.ContainsRune("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", prev)
}

