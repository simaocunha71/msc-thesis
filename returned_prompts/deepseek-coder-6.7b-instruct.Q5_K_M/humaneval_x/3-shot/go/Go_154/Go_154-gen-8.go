    if len(a) != len(b) {
        return false
    }
    temp := a + a
    if strings.Contains(temp, b) {
        return true
    }
    return false
}



