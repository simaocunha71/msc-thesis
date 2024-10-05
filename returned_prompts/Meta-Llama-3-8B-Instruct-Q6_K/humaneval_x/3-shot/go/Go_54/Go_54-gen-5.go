    if len(s0) != len(s1) {
        return false
    }

    s0 = strings.ToLower(s0)
    s1 = strings.ToLower(s1)

    for i := 0; i < len(s0); i++ {
        if strings.Count(s0, string(s0[i])) != strings.Count(s1, string(s0[i])) {
            return false
        }
    }
    return true
} 





