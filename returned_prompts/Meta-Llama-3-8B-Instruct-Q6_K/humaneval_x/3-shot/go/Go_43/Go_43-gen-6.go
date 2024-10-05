    set := make(map[int]bool)
    for _, v := range l {
        if _, b := set[-v]; b {
            return true
        }
        set[v] = true
    }
    return false
}