    if len(txt) < 1 {
        return false
    }
    return strings.HasSuffix(txt, " ") && ('a' <= txt[len(txt)-1] && txt[len(txt)-1] <= 'z')
}



