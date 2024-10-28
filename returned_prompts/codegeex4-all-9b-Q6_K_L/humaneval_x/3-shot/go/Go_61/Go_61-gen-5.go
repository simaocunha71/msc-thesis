    depth := 0
    for _, c := range brackets {
        switch c {
        case '(':
            depth += 1
        case ')':
            depth -= 1
        }
        if depth < 0 {
            return false
        }
    }
    return depth == 0
}



