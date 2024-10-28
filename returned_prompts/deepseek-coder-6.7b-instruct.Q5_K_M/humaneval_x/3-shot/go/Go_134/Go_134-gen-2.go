    if len(txt) == 0 {
        return false
    }

    lastChar := txt[len(txt)-1]
    if !strings.ContainsRune("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", lastChar) {
        return false
    }

    if len(txt) == 1 {
        return true
    }

    prevChar := txt[len(txt)-2]
    return !strings.ContainsRune("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", prevChar)
}



