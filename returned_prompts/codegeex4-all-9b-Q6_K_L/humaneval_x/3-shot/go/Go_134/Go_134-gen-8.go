    if len(txt) == 0 {
        return false
    }
    last_char := txt[len(txt)-1]
    if !strings.ContainsRune("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", last_char) {
        return false
    }
    return !strings.HasSuffix(txt, string(last_char))
}

