    if len(txt) == 0 {
        return false
    }

    last_char := txt[len(txt)-1]
    if !(last_char >= 'a' && last_char <= 'z') && !(last_char >= 'A' && last_char <= 'Z') {
        return false
    }

    if strings.HasSuffix(txt, " ") {
        return false
    }

    return true
}



