    if len(s0) != len(s1) {
        return false
    }
    m := make(map[rune]int)
    for _, c := range s0 {
        m[c] += 1
    }
    for _, c := range s1 {
        m[c] -= 1
        if m[c] < 0 {
            return false
        }
    }
    return true
}



