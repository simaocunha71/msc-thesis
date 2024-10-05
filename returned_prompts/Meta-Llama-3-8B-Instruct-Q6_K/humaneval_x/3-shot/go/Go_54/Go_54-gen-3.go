    if len(s0) != len(s1) {
        return false
    }
    counts := make(map[rune]int)
    for _, c := range s0 {
        counts[c]++
    }
    for _, c := range s1 {
        counts[c]--
    }
    for _, count := range counts {
        if count != 0 {
            return false
        }
    }
    return true
}