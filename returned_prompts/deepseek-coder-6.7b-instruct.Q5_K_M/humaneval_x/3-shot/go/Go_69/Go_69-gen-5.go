    m := make(map[int]int)

    for _, v := range lst {
        _, ok := m[v]
        if ok {
            m[v] += 1
        } else {
            m[v] = 1
        }
    }

    for k, v := range m {
        if k <= v {
            return k
        }
    }
    return -1
}



