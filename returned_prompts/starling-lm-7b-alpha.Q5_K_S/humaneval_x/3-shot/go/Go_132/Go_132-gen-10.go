    depth := 0
    for _, v := range s {
        if v == '[' {
            depth++
        } else {
            depth--
        }
        if depth < 0 {
            return true
        }
    }
    return false
}



