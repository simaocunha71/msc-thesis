    last_char := string(txt[len(txt)-1])
    if strings.ContainsAny(last_char,"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"){
        return true
    }
    return false
}



