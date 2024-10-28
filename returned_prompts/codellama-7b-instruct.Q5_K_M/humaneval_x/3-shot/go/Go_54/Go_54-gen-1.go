    for _, c := range s0 {
        if !strings.Contains(s1, string(c)) {
            return false
        }
    }
    for _, c := range s1 {
        if !strings.Contains(s0, string(c)) {
            return false
        }
    }
    return true
}




