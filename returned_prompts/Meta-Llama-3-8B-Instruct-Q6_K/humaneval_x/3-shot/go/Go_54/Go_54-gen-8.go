    if len(s0) != len(s1) {
        return false
    }
    s0_counts := make(map[rune]int)
    s1_counts := make(map[rune]int)
    for _, c := range s0 {
        s0_counts[c]++
    }
    for _, c := range s1 {
        s1_counts[c]++
    }
    for k, v := range s0_counts {
        if v != s1_counts[k] {
            return false
        }
    }
    return true
}