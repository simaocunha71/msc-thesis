func IsNested(s string) bool {
    count := 0
    for _, c := range s {
        if c == '[' {
            count++
        } else {
            count--
        }
        if count < 0 {
            return false
        }
    }
    return count > 0
}