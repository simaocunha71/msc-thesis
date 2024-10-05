    m := make(map[int]int)
    for _, v := range l {
        m[v]++
    }
    for _, v := range l {
        if m[v] >= 3 {
            return true
        }
        if m[v] >= 2 {
            m[v] = 0
            continue
        }
        for _, w := range l {
            if m[v]+m[w] >= 3 {
                return true
            }
            if m[v]+m[w] >= 2 {
                m[v] = 0
                m[w] = 0
                break
            }
        }
    }
    return false
}



