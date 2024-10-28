    l = l[:0]
    keys := make(map[int]bool)
    for _, v := range l {
        if _, ok := keys[v]; !ok {
            l = append(l, v)
            keys[v] = true
        }
    }
    sort.Ints(l)
    return l
}



