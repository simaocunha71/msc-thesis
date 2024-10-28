    if len(s0) != len(s1) {
        return false
    }

    m := make(map[rune]int)
    for _, r := range s0 {
        m[r] += 1
    }

    for _, r := range s1 {
        if m[r] == 0 {
            return false
        }
        m[r] -= 1
    }

    return true
}



