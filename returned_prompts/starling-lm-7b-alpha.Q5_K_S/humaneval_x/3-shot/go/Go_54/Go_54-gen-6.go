    m0 := make(map[rune]int)
    for _, c := range s0 {
        m0[c] += 1
    }
    for _, c := range s1 {
        m0[c] -= 1
    }
    for _, v := range m0 {
        if v != 0 {
            return false
        }
    }
    return true
}



