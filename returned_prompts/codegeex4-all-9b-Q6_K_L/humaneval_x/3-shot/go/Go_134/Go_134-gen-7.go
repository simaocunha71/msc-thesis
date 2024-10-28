    if len(txt) == 0{
        return false
    }
    if strings.HasSuffix(txt," ") {
        return false
    }
    return strings.ContainsAny(txt, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
}

