    m := make(map[int]int)
    for _, v := range l {
        m[v] += 1
    }
    for _, v := range l {
        if m[v] >= 2 {
            m[v] -= 2
            continue
        }
        for _, u := range l {
            if m[v] > 0 && m[u] > 0 && m[-v-u] > 0 {
                return true
            }
            m[u]--
        }
        m[v]--
    }
    return false
}



