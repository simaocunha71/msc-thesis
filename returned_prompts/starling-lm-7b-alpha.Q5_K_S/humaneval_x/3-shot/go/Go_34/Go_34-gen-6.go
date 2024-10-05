    m := make(map[int]struct{})
    r := make([]int, 0)
    for _, v := range l {
        if _, ok := m[v]; !ok {
            m[v] = struct{}{}
            r = append(r, v)
        }
    }
    sort.Ints(r)
    return r
}



