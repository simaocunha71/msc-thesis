func SameChars(s0 string, s1 string) bool {
    c0 := make(map[rune]bool)
    c1 := make(map[rune]bool)
    for _, c := range s0 {
        c0[c] = true
    }
    for _, c := range s1 {
        c1[c] = true
    }
    for k := range c0 {
        if !c1[k] {
            return false
        }
    }
    for k := range c1 {
        if !c0[k] {
            return false
        }
    }
    return true
}