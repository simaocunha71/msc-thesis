    if len(s0) != len(s1) {
        return false
    }

    for i := range s0 {
        if !strings.Contains(s1, string(s0[i])) {
            return false
        }
    }
    return true
}



