    if len(txt) == 0 {
        return false
    }
    lastChar := txt[len(txt)-1]
    if !strings.Contains("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", lastChar) {
        return false
    }
    if len(txt)-1 > 0 {
        if txt[len(txt)-2] == ' ' {
            return true
        }
    }
    return false
}



