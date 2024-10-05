    if strings.HasSuffix(txt, " ") {
        return false
    }

    last := txt[len(txt)-1]

    if last >= 'a' && last <= 'z' || last >= 'A' && last <= 'Z' {
        return true
    }
    return false
}

