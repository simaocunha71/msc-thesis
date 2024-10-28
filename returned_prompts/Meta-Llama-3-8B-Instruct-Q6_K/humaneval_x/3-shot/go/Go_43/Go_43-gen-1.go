    seen := make(map[int]bool)
    for _, v := range l {
        if _, ok := seen[-v]; ok {
            return true
        }
        seen[v] = true
    }
    return false
}