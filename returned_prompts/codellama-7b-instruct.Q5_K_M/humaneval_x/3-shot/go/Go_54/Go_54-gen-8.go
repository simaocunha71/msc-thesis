    if len(s0) != len(s1) {
        return false
    }

    for i := 0; i < len(s0); i++ {
        for j := 0; j < len(s1); j++ {
            if s0[i] == s1[j] {
                s1 = s1[:j] + s1[j+1:]
                break
            }
        }
    }
    return s1 == ""
}



