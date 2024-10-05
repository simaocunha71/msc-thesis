    var depth int
    for _, c := range s {
        if c == '[' {
            depth++
        }else if c == ']' {
            depth--
        }
        if depth < 0 {
            return true
        }
    }
    return false
}



