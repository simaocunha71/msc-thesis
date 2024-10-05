    if len(s0) != len(s1) {
        return false
    }
    counts0 := make(map[rune]int)
    counts1 := make(map[rune]int)
    for _, c := range s0 {
        counts0[c]++
    }
    for _, c := range s1 {
        counts1[c]++
    }
    for k, v := range counts0 {
        if v != counts1[k] {
            return false
        }
    }
    return true
}