    var currentDepth int
    for _, r := range s {
        switch r {
        case '[':
            currentDepth++
        case ']':
            currentDepth--
        }
        if currentDepth < 0 {
            return true
        }
    }
    return currentDepth > 0
}



