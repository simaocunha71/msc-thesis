    m := make(map[rune]int)

    for _, c := range s0 {
        m[c]++
    }

    for _, c := range s1 {
        m[c]--
        if m[c] < 0 {
            return false
        }
    }

    return len(m) == 0
}



