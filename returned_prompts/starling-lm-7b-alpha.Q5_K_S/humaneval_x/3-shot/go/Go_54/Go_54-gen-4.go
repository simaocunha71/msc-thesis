    if len(s0) != len(s1) {
        return false
    }

    counts0 := make(map[rune]int)
    counts1 := make(map[rune]int)

    for _, c := range s0 {
        counts0[c] += 1
    }
    for _, c := range s1 {
        counts1[c] += 1
    }

    for _, v := range counts0 {
        if v != counts1[c] {
            return false
        }
    }
    return true
}



