    if len(txt) == 0{
        return false
    }
    if strings.HasSuffix(txt, " ") {
        return false
    }

    return txt[len(txt)-1] >= 'a' && txt[len(txt)-1] <= 'z' || txt[len(txt)-1] >= 'A' && txt[len(txt)-1] <= 'Z'
}

