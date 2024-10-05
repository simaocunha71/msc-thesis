    if len(txt)==0 {
        return false
    }
    if strings.IndexAny(txt, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == -1 {
        return false
    }
    if strings.IndexAny(txt, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == len(txt)-1 {
        return false
    }
    return true
}



