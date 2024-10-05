    if len(s0) != len(s1) {
        return false
    }
    for i := 0; i < len(s0); i++ {
        if s0[i] != s1[i] {
            return false
        }
    }
    return true
}



