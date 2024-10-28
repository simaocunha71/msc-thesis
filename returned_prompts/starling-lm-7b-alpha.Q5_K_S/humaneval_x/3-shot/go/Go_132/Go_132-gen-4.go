    depth := 0
    for _, r := range s {
        if r == '[' {
            depth++
        }else if r == ']' {
            depth--
        }
        if depth < 0 {
            return true
        }
    }
    return depth > 0
}



