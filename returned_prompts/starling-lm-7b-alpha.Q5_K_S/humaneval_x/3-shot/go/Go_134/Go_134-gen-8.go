    if len(txt) == 0 {
        return false
    }
    if len(txt) == 1 {
        return txt[0] >= 'a' && txt[0] <= 'z' || txt[0] >= 'A' && txt[0] <= 'Z'
    }
    if txt[len(txt)-1] >= 'a' && txt[len(txt)-1] <= 'z' || txt[len(txt)-1] >= 'A' && txt[len(txt)-1] <= 'Z' {
        if txt[len(txt)-2] >= 'a' && txt[len(txt)-2] <= 'z' || txt[len(txt)-2] >= 'A' && txt[len(txt)-2] <= 'Z' {
            return false
        } else {
            return true
        }
    } else {
        return false
    }
}





