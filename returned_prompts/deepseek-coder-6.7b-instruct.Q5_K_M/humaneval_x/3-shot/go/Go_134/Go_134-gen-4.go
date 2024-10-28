    if len(txt) == 0 {
        return false
    }
    
    lastChar := txt[len(txt)-1]
    if (lastChar >= 'a' && lastChar <= 'z') || (lastChar >= 'A' && lastChar <= 'Z') {
        if len(txt) == 1 || txt[len(txt)-2] == ' ' {
            return true
        }
    }
    return false
}



