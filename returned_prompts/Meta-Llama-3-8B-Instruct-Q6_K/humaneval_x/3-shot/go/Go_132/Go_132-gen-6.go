    var depth int
    for _, c := range s {
        if c == '[' {
            depth++
        } else if c == ']' {
            if depth == 0 {
                return false
            }
            depth--
        }
    }
    return depth > 0
}