    if len(txt) == 0 {
        return false
    }
    last_char := string(txt[len(txt)-1])
    words := strings.Fields(txt)
    if len(words) == 1 && last_char != " " {
        return true
    }
    return false
}



