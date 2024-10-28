func SameChars(s0 string, s1 string) bool {
    c0 := make(map[rune]int)
    c1 := make(map[rune]int)
    for _, c := range s0 {
        c0[c]++
    }
    for _, c := range s1 {
        c1[c]++
    }
    if len(c0) != len(c1) {
        return false
    }
    for k, v := range c0 {
        if v != c1[k] {
            return false
        }
    }
    return true
}