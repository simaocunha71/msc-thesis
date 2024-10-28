    if len(txt) == 0 || !strings.Contains("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", string(txt[len(txt)-1])) {
        return false
    }

    for i := len(txt) - 2; i >= 0; i-- {
        if txt[i] == ' ' && (txt[i+1] >= 'a' && txt[i+1] <= 'z' || txt[i+1] >= 'A' && txt[i+1] <= 'Z') {
            return true
        }
    }

    return false
}



