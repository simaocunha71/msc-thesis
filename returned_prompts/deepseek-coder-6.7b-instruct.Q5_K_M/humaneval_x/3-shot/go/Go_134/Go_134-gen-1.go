    if len(txt) == 0 || !strings.Contains("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", string(txt[len(txt)-1])) {
        return false
    }

    if len(txt) == 1 {
        return false
    }

    return strings.Contains("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", string(txt[len(txt)-2]))
}


