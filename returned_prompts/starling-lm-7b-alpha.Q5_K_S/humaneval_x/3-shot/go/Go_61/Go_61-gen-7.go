    depth := 0
    for _, c := range brackets {
        if c == '(' {
            depth += 1
        }else if c == ')' {
            if depth == 0 {
                return false
            }
            depth -= 1
        }
    }
    return depth == 0
}



