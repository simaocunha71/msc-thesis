    m0 := make(map[rune]int)
    m1 := make(map[rune]int)

    for _, c := range s0 {
        m0[c]++
    }

    for _, c := range s1 {
        m1[c]++
    }

    if len(m0) != len(m1) {
        return false
    }

    for k, v := range m0 {
        if m1[k] != v {
            return false
        }
    }
    return true
}



