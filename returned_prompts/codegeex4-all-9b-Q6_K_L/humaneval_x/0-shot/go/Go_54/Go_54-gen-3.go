func SameChars(s0 string, s1 string) bool {
    if len(s0) != len(s1) {
        return false
    }
    counts := make(map[rune]int)
    for _, c := range s0 {
        counts[c]++
    }
    for _, c := range s1 {
        if counts[c] == 0 {
            return false
        }
        counts[c]--
    }
    return true
}