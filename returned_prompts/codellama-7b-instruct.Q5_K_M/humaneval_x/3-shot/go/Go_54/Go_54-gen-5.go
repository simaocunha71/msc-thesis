    if len(s0) != len(s1) {
        return false
    }
    for i := 0; i < len(s0); i++ {
        if !(strings.Contains(s1, string(s0[i]))) {
            return false
        }
    }
    return true
}



