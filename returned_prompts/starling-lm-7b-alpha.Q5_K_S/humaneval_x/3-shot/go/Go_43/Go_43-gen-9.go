    m := make(map[int]int)
    for _, x := range l {
        if _, ok := m[x]; ok {
            return true
        } else {
            m[0-x] += 1
        }
    }
    return false
}



