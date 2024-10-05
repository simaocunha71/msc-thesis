    if len(txt) == 0 {
        return false
    }

    for i := len(txt) - 1; i >= 0; i-- {
        if !strings.Contains(txt[i], " ") {
            return true
        }
    }
    return false
}
