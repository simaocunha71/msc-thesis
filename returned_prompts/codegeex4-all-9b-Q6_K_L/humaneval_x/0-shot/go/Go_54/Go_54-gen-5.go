func SameChars(s0 string, s1 string) bool {
    count := make(map[rune]int)
    for _, c := range s0 {
        count[c]++
    }
    for _, c := range s1 {
        count[c]--
    }
    for _, c := range count {
        if c != 0 {
            return false
        }
    }
    return true
}