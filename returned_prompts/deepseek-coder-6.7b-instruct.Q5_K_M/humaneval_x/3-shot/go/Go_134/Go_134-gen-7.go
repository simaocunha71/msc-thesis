    if len(txt) == 0 || !strings.HasSuffix(txt, " ") {
        return false
    }

    return txt[len(txt) - 2] >= 'a' && txt[len(txt) - 2] <= 'z' || txt[len(txt) - 2] >= 'A' && txt[len(txt) - 2] <= 'Z'
}



