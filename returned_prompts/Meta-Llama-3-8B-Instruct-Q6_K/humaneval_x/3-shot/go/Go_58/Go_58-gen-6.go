    m1 := make(map[int]bool)
    m2 := make(map[int]bool)
    res := []int{}

    for _, val := range l1 {
        m1[val] = true
    }
    for _, val := range l2 {
        if m1[val] {
            res = append(res, val)
            delete(m1, val)
        }
    }
    sort.Ints(res)
    return res
}