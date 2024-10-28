func IsNested(s string) bool {
    open, close := 0, 0
    for _, c := range s {
        if c == '[' {
            open++
        } else if c == ']' {
            close++
        }
        if close > open {
            return false
        }
    }
    return open == close
}