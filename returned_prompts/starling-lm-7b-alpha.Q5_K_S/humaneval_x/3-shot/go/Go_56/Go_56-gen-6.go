    currentDepth := 0
    for _, bracket := range brackets {
        switch bracket {
        case '<':
            currentDepth += 1
        case '>':
            if currentDepth == 0 {
                return false
            }
            currentDepth -= 1
        }
    }
    return currentDepth == 0
}



