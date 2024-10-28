    m := make(map[int]int)

    for _, e := range l {
        if _, ok := m[e]; ok {
            return true
        }
        m[e]++
    }
    return false
}



