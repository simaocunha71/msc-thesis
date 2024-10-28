    seen := make(map[int]bool, len(l))
    for _, i := range l {
        if seen[i] {
            return true
        }
        seen[i] = true
    }
    return false
}



