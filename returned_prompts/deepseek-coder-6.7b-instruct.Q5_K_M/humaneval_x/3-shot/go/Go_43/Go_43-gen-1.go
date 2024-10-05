    m := make(map[int]bool)
    for _, num := range l {
        if _, ok := m[-num]; ok {
            return true
        }
        m[num] = true
    }
    return false
}



