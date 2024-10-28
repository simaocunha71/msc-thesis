    depth := 0
    for _, ch := range s {
        if ch == '[' {
            depth += 1
        }else if ch == ']' {
            depth -= 1
        }
        if depth < 0 {
            return true
        }
    }
    return false
}



