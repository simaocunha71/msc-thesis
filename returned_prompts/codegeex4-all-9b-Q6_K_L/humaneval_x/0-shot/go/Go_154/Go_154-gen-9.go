func CycpatternCheck(a , b string) bool {
    n := len(b)
    for i := 0; i < n; i++ {
        t := b[i:] + b[:i]
        if strings.Contains(a, t) {
            return true
        }
    }
    return false
}